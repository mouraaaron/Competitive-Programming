# -*- coding: utf-8 -*-

linha1 = input().split()
A = int(linha1[0])
B = int(linha1[1])

if (A % B == 0) or (B % A == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
    
