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

""" VARIAVEIS
    pessoas : DICIONARIO DE STRING -> INTEIRO (Armazena Nome e Idade)
    pessoas_autorizadas : LISTA DE STRING
    pessoas_desautorizadas : LISTA DE STRING
    nome : STRING
    idade : INTEIRO

INICIO
    // Inicialização
    LIMPAR TELA
    EXIBIR "Entrada de evento para maiores de idade 🔞"
    EXIBIR "------------------------------------------"

    // Loop de Cadastro e Verificação
    REPETIR
        // 1. Coletar Nome
        LER nome DE "Seja-bem vindo, gostaria que informa-se seu nome ou digite [p] para sair: "
        
        // 2. Condição de Saída
        SE (nome for igual a "p") ENTAO
            SAIR DO REPETIR
        FIM SE

        // 3. Coletar Idade e Tratar Erro
        TENTAR
            LER idade DE "Seja-bem vindo, gostaria que informa-se sua idade: "
            CONVERTER idade PARA INTEIRO
            
            // 4. Armazenar Dados
            ADICIONAR (nome, idade) AO DICIONARIO pessoas
            
            // 5. Exibir o Registro
            EXIBIR "\nLista de pessoas registradas"
            PARA CADA (chave, valor) EM pessoas FAZER
                EXIBIR " REGISTROS 😁 = " + chave + ": " + valor + " anos"
            FIM PARA
            
            // 6. Verificar Idade e Autorização
            SE (idade FOR MAIOR OU IGUAL A 18) ENTAO
                ADICIONAR nome À pessoas_autorizadas
            SENAO
                ADICIONAR nome À pessoas_desautorizadas
            FIM SE
            
        EXCETO ERRO DE CONVERSÃO (ValueError)
            EXIBIR "Idade inválida ❌😒"
            
        FIM TENTAR
    FIM REPETIR

    // Exibição dos Resultados Finais
    EXIBIR "\nPessoas autorizadas a entrar : " + pessoas_autorizadas + " 😁"
    EXIBIR "\n----------------------------------------------------------"
    EXIBIR "Pessoas desautorizadas a entrar: " + pessoas_desautorizadas + " 😒"
FIM ALGORITMO """

