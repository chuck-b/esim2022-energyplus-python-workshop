from pyenergyplus.plugin import EnergyPlusPlugin

class new_function(EnergyPlusPlugin):

    def __init__(self):
        super().__init__()

        self.e = self.api.exchange

        # handles
        self.need_to_get_handles = True
        self.variables = {}
        self.actutators = {}
        self.globals = {}

    def get_handles(self, state):
        
        # add some variables
        self.variables['t_out'] = self.e.get_variable_handle(state, "Site Outdoor Air Drybulb Temperature", "Environment")

        self.need_to_get_handles = False

    def handles_are_valid(self, state) -> bool:
        handles_are_valid = True
        handles = {**self.actuators, ** self.variables, **self.globals}
        for (k,v) in handles.items():
            if v == -1:
                handles_are_valid = False
                # print(k,v)
                self.api.runtime_issue_severe(state, f"Handle not found for '{k}'")
        return handles_are_valid

    
    def on_begin_timestep_before_predictor(self, state) -> int:
        # make sure we are all set up
        if not self.e.api_data_fully_ready(state):
            return 0
        if self.need_to_get_handles:
            self.get_handles(state)
        if not self.handles_are_valid(state):
            return 1 #aka bad
        
        ###
        # insert something else here

        ###
        return 0