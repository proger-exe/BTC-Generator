import random
import os

class System:
    def printf(text):
        os.system(f'echo {text}')

    def BTCGEN(text=None):
        System.printf(f'[BTCCheckGen] {text}')
    
    def generate_checks(cicles):
        chars = 'aedfgc1234567890'
        for i in range(cicles):
            password =''
            for i in range(32):
                password += random.choice(chars)
            print(f'https://t.me/BTC_CHANGE_BOT?start=c_{password}')

System.BTCGEN()

System.printf('Генератор чеков для @BTC_CHANGE_BOT\n')



System.printf('Укажите желаемое количество ссылок для генерации: \n')

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
