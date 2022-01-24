
from cv2 import dft
from iqoptionapi.stable_api import IQ_Option
import time

##from finta import TA
##from time import time,sleep
##from datetime import datetime
##import pandas as pd


API = IQ_Option ('hobsonbmn.trader@gmail.com','natalia12')
API.connect()

API.change_balance('PRACTICE') # PRACTICE / REAL


if API.check_connect():
    print('Conectado com Sucesso!')
else: 
    print('Erro ao Conectar')
    input('\n\n Aperte enter para Sair')
    exit()

##def get_data(par,timeframe,periods = 200):
    ##global API
    ##velas = API.get_candles(par,timeframe*60,periods,time())
    ##df = pd.DataFrame(velas)
    ##df.rename(columns={"max":"high","min":"low"},inplace=True)
    ##return df
#def MovAvarDev(df, periods = 20):
 #src = TA.SSMA(df,periods)
 #calc = df.iloc[-1]['close']-src.iloc[-1]
 #return calc ,'green' if calc>= (df.iloc[-]['close'] - src.iloc[-2]) else 'red'
 #def entrada (par,dir,timeframe):
    #global API

#print('\n Abrindo operação') 
#status,id = API.buy_digital_spot_v2(par,dir,timeframe)
#if status:
    #status = False
    #while status == False:
        #status, lucro = API.check_win_digital_v2(id)
        #if lucro > 0:
             #print('WIN,LUCRO DE',lucro)
        #else:
             #print('LOSS,PERCA DE',lucro)
#else:
    #print('Erro ao abrir operação \ n',id)
    #print('\n')
    
par = 'EURUSD'
timeframe = 15

#while True:
#df =get_data(par,timeframe,200)
#taxa,cor = MovAvarDev(df,20)
#ssma_3 = TA.ssma(df,3)
#ssma_3 = TA.ssma(df,50)
#if ssma_3.iloc[-1]<=ssma_50.iloc[-1] and ssma_3.iloc[-2]>ssma_50.iloc[-2] and color == 'red':
    #entrada(par,'put',timeframe)




payout = API.get_digital_payout(par)
print(payout)

status, id = API.buy_digital_spot_v2(par,2000,'call', 15)

print(status ,id) 

