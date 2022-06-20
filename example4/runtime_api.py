from pathlib import Path
import subprocess
import sys

energyplus_install_dir = Path("/Applications/EnergyPlus-22-1-0/")
idf_file_relative = Path("example4/1ZoneUncontrolled.idf")
weather_file_realtive = Path("./weatherfiles/USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw")
output_relative_directory=Path('./example4/sim')

# insert the repo build tree or install path into the search Path, then import the EnergyPlus API
sys.path.insert(0, str(energyplus_install_dir))
from pyenergyplus.api import EnergyPlusAPI

def my_function(state):
    
    if api.exchange.api_data_fully_ready(state): #Necessary condition
        if api.exchange.warmup_flag(state) == 0:
            To_handle = api.exchange.get_variable_handle(state, "Site Outdoor Air Drybulb Temperature", "Environment")


            To = api.exchange.get_variable_value(state, To_handle)
            print(f"Outdoor Temp: {To:.2f}")
            #return (To)

def print_process(val):
    print(val)


api = EnergyPlusAPI()

state = api.state_manager.new_state() #Necessary condition
api.state_manager.reset_state(state)

#api.runtime.callback_begin_zone_timestep_after_init_heat_balance(state, my_function)
api.runtime.callback_progress(state,print_process)

api.runtime.run_energyplus(state,
    [
        '-d', f"{output_relative_directory}",
        '-w',f"{weather_file_realtive}",
        f"{idf_file_relative}"
    ]
)
