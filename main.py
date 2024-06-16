import random

all_symbols = 'QWERTZUIOPASDFGHJKLYXCVBNMqwertzuiopasdfghjklyxcvbnm1234567890!?.'
length = int(input('Выберите количество символов для генерации пароля.'))
password = ''

for i in range(length):
    password += random.choice(all_symbols)
    
    
print('Ваш сгенерированный пароль:', password)
