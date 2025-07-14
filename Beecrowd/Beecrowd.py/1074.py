# -*- coding: utf-8 -*-
n = int(input())
numeros = []

for _ in range(n):
    X = int(input())
    numeros.append(X)

for X in numeros:
    if X == 0:
        print('NULL')
    else:
        paridade = 'EVEN' if X % 2 == 0 else 'ODD'
        sinal = 'POSITIVE' if X > 0 else 'NEGATIVE'
        print(f'{paridade} {sinal}')
