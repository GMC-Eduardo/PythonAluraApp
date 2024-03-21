import os

def exibir_tela():
    print('Veja se é par ou impar o número!')

def extrair_digito_usuario():
    numero = int(input('Digite um número: '))
    os.system('cls')
    return numero

def check_par_impar(numero):    
    if  (numero % 2 == 0):
        print('é par!')
    else:
        print('é impar!')

def main():
    exibir_tela()
    
    check_par_impar(extrair_digito_usuario())
    
if __name__ == '__main__':
    main()