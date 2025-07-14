# -*- coding: utf-8 -*-

linha = input().split()
n1 = int(linha[0])
n2 = int(linha[1])
n3 = int(linha[2])

nums = [n1, n2, n3]

ordenado = sorted(nums)

for v in ordenado:
    print(v)

print()

print(n1)
print(n2)
print(n3)
