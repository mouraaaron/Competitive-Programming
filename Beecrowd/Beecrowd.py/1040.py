# -*- coding: utf-8 -*-

linha1 = input().split()
N1 = float(linha1[0])
N2 = float(linha1[1])
N3 = float(linha1[2])
N4 = float(linha1[3])

MEDIA = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4)) / 10
print(f'Media: {MEDIA:.1f}')

if (MEDIA >= 7):
    print('Aluno aprovado.')
elif (MEDIA < 5):
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    NE = float(input())
    print(f'Nota do exame: {NE:.1f}')
    NOTA = (MEDIA + NE)/2
    if NOTA >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {NOTA:.1f}')