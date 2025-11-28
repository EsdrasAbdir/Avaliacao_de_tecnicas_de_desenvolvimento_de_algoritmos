""" Criar um programa em Python 
que simule um sistema de verificação de idade para entrada em eventos. """


import os

os.system('cls')


print('Entrada de evento para maiores de idade 🔞')
print('------------------------------------------')


pessoas = {

    }

pessoas_autorizadas = []
pessoas_desautorizadas = []
while True:
        nome = input('Seja-bem vindo, gostaria que informa-se seu nome ou digite [p] para sair: ')
        if nome.lower() == 'p':
            break
        try:
            idade = int(input('Seja-bem vindo, gostaria que informa-se sua idade: '))
            pessoas[nome] = idade
            print('\nLista de pessoas registradas')
            for pessoa, idade in pessoas.items():
                 print(f' REGISTROS 😁 =   {nome}: {idade} anos')
            if idade >= 18:
                pessoas_autorizadas.append(nome)
            else: 
                 pessoas_desautorizadas.append(nome)        

        except ValueError:
            print('Idade inválida ❌😒')

print(f'\nPessoas autorizadas a entrar : {pessoas_autorizadas} 😁')
print('\n----------------------------------------------------------')
print(f'Pessoas desautorizadas a entrar: {pessoas_desautorizadas} 😒')

#                              Pseudo-código do programa

"""
Inicialização

Exiba 'Entrada de evento para maiores de idade 🔞'
Exiba '------------------------------------------'

criar variável do tipo dict chamado pessoas

criar uma variável do tipo lista chamadas pessoas autorizadas

criar uma variável do tipo lista chamadas pessoas desautorizadas

Iniciar laço de repetição enquanto verdadeiro

Solicita variável nome

Se nome for igual a 'p' pare

Tentar

Solicitar variável idade do tipo inteiro

Adicionar variável nome e idade no dicionário pessoas

Exiba 'Lista de pessoas registradas'

Iterar em cada pessoa com sua respectiva idade no dicionário

Exiba ' REGISTROS 😁 =   {nome}: {idade} anos'

Se idade for maior ou igual a 18 adicionar nome na lista pessoas autorizadas

Caso contrário adicionar nome na lista de pessoas desautorizadas

Exceção do tipo ValueError exiba 'Idade inválida ❌😒'

Exiba 'Pessoas autorizadas a entrar : {pessoas_autorizadas} 😁'

Exiba '----------------------------------------------------------'

Exiba 'Pessoas desautorizadas a entrar: {pessoas_desautorizadas} 😒' """

