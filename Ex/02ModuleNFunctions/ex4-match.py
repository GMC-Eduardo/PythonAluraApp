import os

def exibe_tela():
    print('Descubra em qual quadrante o ponto se encontra! (★^O^★)')

def extrair_x():
    x = int(input('Digite o valor de X: '))
    os.system('cls')
    return x

def extrair_y():
    y = int(input('Digite o valor de Y: '))
    os.system('cls')
    return y

def busca_quadrante(x, y):
    match (x > 0, y > 0):
        case (True, True):
            print('Primeiro Quadrante! (๑>ᴗ<๑)')
        case (False, True):
            print('Segundo Quadrante! (◕‿◕✿)')
        case (False, False):
            print('Terceiro Quadrante! (◠‿◠✿)')
        case (True, False):
            print('Quarto Quadrante! (◕‿◕)♡')
        case _:
            print('O ponto está localizado no eixo ou na origem.')

def main():
    exibe_tela()
    x = extrair_x()
    y = extrair_y()
    busca_quadrante(x, y)

if __name__ == '__main__':
    main()
