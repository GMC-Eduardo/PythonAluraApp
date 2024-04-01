import os

dicionario = {'a': 1, 'b': 2, 'c': 3}
# professor
# pessoa = {'nome': ‘Amanda', 'idade': 19, 'cidade': 'São Luís'}
# if 'nome' in pessoa:
#     print("A chave 'nome' existe no dicionário.")
# else:
#     print("A chave 'nome' não existe no dicionário.")

def listar_dicionario():
    i = 0
    for chave,valor in dicionario.items():
        
        print(f'Chave : {chave} - valor  {valor}')
def testa_chave():
    chave_teste = input('Digite uma chave para verificar se ela está no dicionário: ')
    if chave_teste in dicionario:
        print(f'A chave {chave_teste} existe no dicionário.')
    else:
        print(f'A chave {chave_teste} não existe no dicionário.')

def main():
        os.system('cls')
        listar_dicionario()
        testa_chave()

        
if __name__ == '__main__':
        main()

