
from iqoptionapi.stable_api import IQ_Option
import time

API = IQ_Option ('hobsonbmn.trader@gmail.com','natalia12')
API.connect()

API.change_balance('PRACTICE') # PRACTICE / REAL

if API.check_connect():
    print('conectado com sucesso!')
else: 
    print('Erro ao conectar')
    input('\n\n Aperte enter para sair')
    exit()

par = 'EURUSD'
timeframe = 15
payout = API.get_digital_payout(par)
print(payout)

status, id = API.buy_digital_spot_v2(par,2,'call', 15)

print(status ,id) 

