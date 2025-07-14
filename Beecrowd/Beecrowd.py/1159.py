# -*- coding: utf-8 -*-

while True:
    X = int(input())
    if X == 0:
        break

    if X % 2 != 0:  
        X += 1      
    soma = 0
    for i in range(5):
        soma += X + 2 * i

    print(soma)
