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
