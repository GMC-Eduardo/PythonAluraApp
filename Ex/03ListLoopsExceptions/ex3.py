
def somar_numeros():
    soma = 0
    for numero in range(11):
        if(numero % 2 != 0):
            soma = numero + soma

    print(f'Soma dos numeros impares é {soma}')


def main():
    somar_numeros()
    

if __name__ == '__main__':
    main()
    
# solucao correto
#     soma_impares = 0
# for i in range(1, 11, 2):
#     soma_impares += i
# print(soma_impares)
