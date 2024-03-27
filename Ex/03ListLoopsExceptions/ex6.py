

def cadastra_numero(): 
    try:  
        numero = int(input('Por favor, digite um numero : '))
        return numero
    except:
        opcao_invalida()

def opcao_invalida():
    print('Lista de elementos inválida, impossivel somar!\n')
    main()

def soma_lista(lista_de_elementos):
    soma = 0
    try:
        for numero in lista_de_elementos:
            soma += numero
        print(f'Soma dos elementos da lista deu: {soma}')
    except:
        opcao_invalida()
   
def main():
    lista_de_elementos = [1,3,5,7,9]
    soma_lista(lista_de_elementos)
    #cadastra_numero()
    
if __name__ == '__main__':
    main()
