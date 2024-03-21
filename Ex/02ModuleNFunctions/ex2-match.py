import os

def exibir_tela():
    print('Olá quer descobrir qual fase da vida você está?\n')

def extrair_idade():
    idade = int(input('Digite sua idade:'))
    os.system('cls')
    return idade

def busca_fase(idade):
    match idade:
        case i if i <= 12:
            print('Criança!')
        case i if i <= 18:
            print('Adolescente!')
        case _:
            print('Adulto!')

def main():
    exibir_tela()
    busca_fase(extrair_idade())

if __name__ == '__main__':
    main()
