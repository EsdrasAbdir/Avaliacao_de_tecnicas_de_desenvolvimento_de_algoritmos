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
        


#                          Pseudo-código desse programa

""" 

importar a biblioteca random
importar a biblioteca Limpar

variável contador igual a 1
variável número igual a 1 até 101

Limpar terminal

Exiba 🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎Contador de 1 até 100 usando o loop for para números pares🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎

iterar e iniciar loop de repetição começando do contador dentro do número

Se o módulo do contador por 2 for igual a 0

Exiba contador


"""

