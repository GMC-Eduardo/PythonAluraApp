import os

def exibe_tela():
    print('Descubra qual quadrante que o ponto se encontra!')

def extrair_x():
    x = int(input('Digite o valor de X: '))
    os.system('cls')
    return x

def extrair_y():
    y = int(input('Digite o valor de y: '))
    os.system('cls')
    return y

def busca_quadrante(x,y):
    if(x > 0 and y > 0):
        print('Primeiro Quadrante!')
    elif(x < 0 and y > 0):
        print('Segundo Quadrante!')
    elif(x < 0 and y < 0):
        print('Terceiro Quadrante!')
    elif(x > 0 and y < 0):
        print('Quarto Quadrante!')
    else:
        print('O ponto está localizado no eixo ou origem.')

def main():
    exibe_tela()
    x = extrair_x()
    y = extrair_y()
    busca_quadrante(x,y)

if __name__ == '__main__':
    main()