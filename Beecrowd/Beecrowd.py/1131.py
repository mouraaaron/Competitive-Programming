# -*- coding: utf-8 -*-
contagemi = 0
contagemg = 0
empates = 0 #tem que fazer os empates ainda
grenais = 1


gols = input().split()
golinter = int(gols[0])
golgremio = int(gols[1])
if golinter > golgremio:
    contagemi += 1
else:
    contagemg += 1

if golinter == golgremio:
    empates += 1




while True:
    print('Novo grenal (1-sim 2-nao)')
    resposta = int(input())
    if resposta == 1:
        grenais += 1
        gols = input().split()
        golinter = int(gols[0])
        golgremio = int(gols[1])
        if golinter > golgremio:
            contagemi += 1
        elif golinter == golgremio:
            empates += 1
        else:
            contagemg += 1
    else:
        print(f'{grenais} grenais')
        print(f'Inter:{contagemi}')
        print(f'Gremio:{contagemg}')
        print(f'Empates:{empates}')
        if contagemi > contagemg:
            print('Inter venceu mais')
        else:
            print('Gremio venceu mais')
        break
        