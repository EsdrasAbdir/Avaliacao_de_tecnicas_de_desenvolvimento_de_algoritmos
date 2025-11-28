""" Desenvolver um sistema simples de cadastro de produtos com nome e preço,
 armazenando em dicionário. """
import os
os.system('cls')
dicionario_de_produtos = {

}
try:
    while True:
        
        produto = input('Digite o nome do produto a ser cadastrado ou [s] para sair🧐: ')
        if produto.lower() == 's':
            break
        elif produto == '':
            print('Produto inválido😒')
            continue
        else:
            preco_do_produto = float(input('Digite o preço do produto💵: '))
            dicionario_de_produtos[produto] = preco_do_produto


    print('------------------------😎Lista de produtos e preços😎----------------------------------')
    print()
    for item, preco_do_produto in dicionario_de_produtos.items():
        print(f'Nome do produto: {item} / preço: {preco_do_produto}💰R$')
except ValueError:
    print('Preço inválido❌❌❌')