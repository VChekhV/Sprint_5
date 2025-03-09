from random import randint

class Person:
    user_name = 'Виталий'
    email = f'Ampilov_15@gmail.com'
    password = f'Shapka1'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@gmail.com'
    password = f'{randint(1000, 9999)}Qwe'