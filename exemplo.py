from iqoptionapi.stable_api import IQ_Option
from finta import TA 
from time import time, sleep
from datetime import datetime
import pandas as pd

API = IQ_Option ('hobsonbmn.trader@gmail.com','natalia12')
API.connect()

API.change_balance('PRACTICE') # PRACTICE / REAL

if API.check_connect():
    print('conectado com sucesso!')
else: 
    print('Erro ao conectar')
    input('\n\n Aperte enter para sair')
    exit()

def get_data (par,timeframe,periods = 200):
    global API
    
    velas = API.get_candles(par,timeframe * 60 , periods,time())
    
    df = pd.DataFrame(velas)
    df.rename(columns={"max":"high","min":"low"},inplace=True)
    
    return df
def MovAvarDev(df,periods = 20):
    src = TA.SSMA(df,periods)
    
    calc = df.iloc[-1]['close'] - src.iloc[-1]
    
    
    return calc, 'green' if calc >= (df.iloc[-2]['close'] - src.iloc[-2]) else 'red'

def entrada (par , dir,timeframe):
    global API
    
    print('\n Abrindo operação')
    status,id = API.buy_digital_spot_v2(par,dir,timeframe)
    
    if status:
        status = False 
        while status == False:
        
    else:
        print('Erro ao abrir a operação\n',id)
        
        print('\n')
    
    