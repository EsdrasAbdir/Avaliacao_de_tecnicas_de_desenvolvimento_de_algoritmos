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

