""" Desenvolver um contador de 1 a 100 com for e outro com while, exibindo apenas números pares.
 """


import random 
import os
contador = 1

numero = range(1,101)

os.system('cls')

print('🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎Contador de 1 até 100 usando o loop for para números pares🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎')
# Usando o loop for

for contador in numero:
    if contador % 2 == 0:
        print(contador)
        contador += 1


