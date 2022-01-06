import random
import os
import json
from requests import get

app_version = "0.2"

class System:

    def printf(text):
        os.system(f'echo {text}')

    def check_update():
        vers = System.get_vers()
        if vers == app_version:
            System.printf('Обновлений нет')
        else:
            System.printf(f'Есть обновление! Обновите софт!')    

    def BTCGEN(text=None):
        System.printf(f'[BTCCheckGen] {text}')
    
    def generate_checks(cicles):
        chars = 'aedfgc1234567890'
        for i in range(cicles):
            password =''
            for i in range(32):
                password += random.choice(chars)
            print(f'https://t.me/BTC_CHANGE_BOT?start=c_{password}')
    
    def get_vers():
        a = get('https://elezor-dev.github.io/api/getvers').text
        data = json.loads(a)
        vers = data["actual_version"]
        return vers

System.printf('Обновления:')
System.check_update()
print()
System.printf('Укажите желаемое количество ссылок для генерации:')

while True:
    try:
        global cicles
        cicles = int(input('>>> '))
        break
    except:
        System.printf('Введено не число!')


System.generate_checks(cicles)

System.printf('ВНИМАНИЕ: Скрипт генерирует рандомные чеки, проверять на валидность придется вручную.')

System.printf('Все новости и обновления в тг канале: @ready_code.')

System.BTCGEN('Чеки сгенерированны!')
