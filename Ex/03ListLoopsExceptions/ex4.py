
def listar_numeros_invertido():
    numero = 10
    while numero >= 0:
       print(f'Numero: {numero}')
       numero-=1


def main():
    listar_numeros_invertido()
    

if __name__ == '__main__':
    main()

# solucao correta
    # for i in range(10, 0, -1):
    # print(i)
