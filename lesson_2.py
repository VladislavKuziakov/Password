import random

symbol_1 = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
symbol_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol_3 = "abcdefghijklnopqrstuvwxyz1234567890"
num_1 = int(input("Введите длину в вашего пароля: "))
num_2 = int(input("Введите длину в вашего ника: "))
password = ''
nick = ''

for i in range(num_1):
    password += random.choice(symbol_1)

nick += random.choice(symbol_2)

for i in range(num_2-1):
    nick += random.choice(symbol_3)

print("Ваш пароль:", password)
print("Ваш ник:", nick)