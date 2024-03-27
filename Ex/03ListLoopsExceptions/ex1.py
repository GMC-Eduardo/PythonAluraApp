#jeito 1

lista_de_numeros = [1,2,3,4,5,6,7,9,10]
lista_de_nomes = ['João','Tamila','Forger','Jorge']
lista_de_ano = [2024,2020]

#jeito 2

lista_de_numeros = [list(range(1,11))]
lista_de_nomes = ['nome1','nome2','nome3','nome4']
lista_de_ano = [2020,2024]

#jeito 3

lista_de_numeros = []
for i in range(1, 11):
    lista_de_numeros.append(i)

for i in range(5):
    match i:
        case 1:
            lista_de_nomes.append('João')
        case 2:
            lista_de_nomes.append('Tamila')
        case 3:             
            lista_de_nomes.append('Forger')
        case 4:             
            lista_de_nomes.append('Jorge')
        case _:
            pass
for i in range(3):
    match i:
        case 1:
            lista_de_ano.append(2020)
        case 2:
            lista_de_ano.append(2024)
        case _:
            pass
#jeito 4
    lista_de_numeros = list(range(1, 11))
    lista_de_nomes = []  # Inicializamos a lista vazia
i = 1
while i <= 4:
    lista_de_nomes.append(f'nome{i}')  # Adicionamos nomes fictícios à lista
    i += 1

ano_nascimento = 2020
ano_atual = 2024
lista_de_ano = [ano_nascimento, ano_atual]

#jeito 5 pedindo para o usuário
import os

lista_de_nomes = []
def exibir_tela():
    print('Resolução do problema 1: \n')
    print('------------------------')
    print('Números de 1 a 10:')
    for i in range(10):
        print(f'Número: {i}')

def cadastra_nome(lista_de_nomes):  
    lista_de_nomes = []
    try:  
        for i in range(4):
            lista_de_nomes.append(input('Por favor me fale um nome: '))
        listar_nomes(lista_de_nomes)
    except:
        opcao_invalida()
def listar_nomes(lista_de_nomes):
    print("\nListando nomes!")
    for nome in lista_de_nomes:
        print(f"Nome: {nome}")

def cadastra_ano(): 
    lista_de_ano = []
    try:  
        ano_nascimento = input('Por favor, diga o ano de nascimento: ')
        ano_atual = input('Por favor, diga o ano atual: ')
        listar_ano(ano_nascimento,ano_atual)
    except:
        opcao_invalida()

def listar_ano(ano_nascimento,ano_atual):
    print("\nAnos informados:")
    print(f"Ano de nascimento: {ano_nascimento}")
    print(f"Ano atual: {ano_atual}")

def opcao_invalida():
    print('Opção inválida cadastre novamente!\n')

def main():
    lista_de_nomes = []
    exibir_tela()
    cadastra_nome(lista_de_nomes)
    cadastra_ano()

if __name__ == '__main__':
    main()
