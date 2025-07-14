# -*- coding: utf-8 -*-
cont1 = 0
cont2 = 0
cont3 = 0

n = int(input())
while n != 4:
    if n == 1:
        cont1 += 1
    elif n == 2:
        cont2 += 1
    elif n == 3:
        cont3 += 1
    n = int(input())

print('MUITO OBRIGADO')
print(f'Alcool: {cont1}')
print(f'Gasolina: {cont2}')
print(f'Diesel: {cont3}')
