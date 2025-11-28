""" Criar um programa que receba nomes de alunos e armazene em uma lista, 
permitindo exibir todos os nomes ao final. """
import os

lista_de_alunos = []

os.system('cls')

while True:
    nome_para_add_na_lista = input('Digite o nome do aluno(a) ou [s] para sair: ')
    if nome_para_add_na_lista.lower() == 's':
        break
    elif nome_para_add_na_lista == '':
        print('nome inválido❌😒')
    else:
        lista_de_alunos.append(nome_para_add_na_lista)

print('----------------------------🤷Lista de Alunos🤷‍♀️-------------------------------------')
print()
for aluno in lista_de_alunos:
    print(aluno)
    print()


#                    Pseudo-código 

"""  
Iniciar

Criar uma variável lista para armazenar dados 

Iniciar laço de repetição enquanto verdadeiro

Solicitar variável aluno ao usuário

Se variável aluno for igual a 's' pare.

Senão se variável aluno for uma string vazia  exiba 'nome inválido❌😒'

Caso contrário Adiciona na variável lista o nome

Exiba '----------------------------🤷Lista de Alunos🤷‍♀️-------------------------------------'

Exiba Nada para pular linha

Iniciar laço de repetição para iterar nos alunos da lista e exiba a váriavel aluno

Exiba Nada para pular linha

"""