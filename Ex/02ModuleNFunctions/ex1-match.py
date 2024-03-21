import os

def exibir_tela():
    print('Veja se é par ou ímpar o número!')

def extrair_digito_usuario():
    numero = int(input('Digite um número: '))
    os.system('cls')
    return numero

def check_par_impar(numero):
    match numero:
        case n if n % 2 == 0:
            print('É par!')
        case _:
            print('É ímpar!')

def main():
    exibir_tela()
    check_par_impar(extrair_digito_usuario())
    
if __name__ == '__main__':
    main()
