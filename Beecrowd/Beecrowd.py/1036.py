# -*- coding: utf-8 -*-

linha1 = input().split()
A = float(linha1[0])
B = float(linha1[1])
C = float(linha1[2])

DELTA = (B ** 2) - 4 * A * C
if DELTA < 0 or A == 0:
    print('Impossivel calcular')
else:
    R1 = (-B + DELTA ** 0.5) / (2 * A)
    R2 = (-B - DELTA ** 0.5) / (2 * A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')