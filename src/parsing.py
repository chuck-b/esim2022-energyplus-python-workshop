import pandas as pd
from datetime import datetime

def parse_energyplus_datetime_string(st:str, year=2021)->datetime:
    st=st.strip()
    month=int(st[0:2])
    day=int(st[3:5])
    hour=int(st[7:9])
    minute=int(st[10:12])
    second=(st[13:15])
    if not hour==24:
        dt=pd.Timestamp(year,month,day,hour,minute)
    else:
        hour=0
        dt=pd.Timestamp(year,month,day,hour,minute)
        dt+=pd.Timedelta('1 day')
    return dt

def print_subprocess_results(result):
    print('---ARGS---\n',result.args)
    print('---RETURNCODE---\n',result.returncode, '(SUCCESS)' if result.returncode==0 else '(FAIL)')
    print('---STDOUT---\n',result.stdout.decode())
    print('---STDERR---\n',result.stderr.decode())