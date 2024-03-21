import os 

def exibir_tela():
    print('Olá quer descobrir qual fase da vida você está?\n')

def extrair_idade():
    idade = int(input('Digite sua idade:'))
    os.system('cls')
    return idade
def busca_fase(idade):
    if idade <= 12:
        print('Criança!')
    elif idade <= 18:
        print('Adolescente!')
    else:
        print('Adulto!')

def main():
    exibir_tela()
    busca_fase(extrair_idade())




if __name__ == '__main__':
    main()