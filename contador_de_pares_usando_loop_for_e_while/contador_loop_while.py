#Contador de 1 até 100 usando o loop while para números pares 😁

import os

numero = 1

os.system('cls')

print('🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎Contador de 1 até 100 usando o loop while🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎🐎')
while numero < 101:
    if numero % 2 == 0:
        print(numero)
        numero += 1
    else:
        numero += 1
