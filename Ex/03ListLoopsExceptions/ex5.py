
def cadastra_numero(): 
    try:  
        numero_tabuada = int(input('Por favor, digite um numero : '))
        return numero_tabuada;
    except:
        opcao_invalida()

def opcao_invalida():
    print('Opção inválida digite um numero valido!\n')
    main()

def calcula_tabuada(numero_tabuada):
    numero = 1
    while numero <= 10:
        print(f"{numero_tabuada} x {numero} = {numero*numero_tabuada}"  )
        numero+=1


def main():
    calcula_tabuada(cadastra_numero())
    
if __name__ == '__main__':
    main()
