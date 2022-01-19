from iqoptionapi.stable_api import IQ_Option
from finta import TA 
from time import time, sleep
from datetime import datetime

API = IQ_Option ('login,senha')
API.connect(host='', port=0, timeout=None, source_address=None)

API.change_balance('PRACTICE') # PRACTICE / REAL

if API.check_connect():
    print('conectado com sucesso!')
else: 
    print('Erro ao conectar')
    input('\n\n Aperte enter para sair')
    exit()
    