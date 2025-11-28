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


#                          Pseudo-código


""" 
Inicializar

Tentar

Iniciar laço de repetição

Solicitar a variável produto

Se o produto for igual a 's', pare o programa

Senão se produto for igual a nada exiba 'Produto inválido😒' e continue

Caso contrário Solicitar a variável preco do produto e guardar a variavel em um dicionário com o produto sendo chave e preço sendo valor

Saindo do laço de repetição exiba ''------------------------😎Lista de produtos e preços😎----------------------------------'

Exiba nada para pular linha

inicie outro laço de repetição para iterar no item e preço de produto no dicionário e exiba item e valor

Excecão exiba 'Preço inválido❌❌❌'














"""