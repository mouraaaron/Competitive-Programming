# -*- coding: utf-8 -*-

N1 = float(input())
N2 = float(input())
N3 = float(input())
N4 = float(input())
N5 = float(input())
N6 = float(input())

Valores = [N1, N2, N3, N4, N5, N6]

contagem = 0

for i in Valores:
    if i > 0:
        contagem += 1

print(f'{contagem} valores positivos')
