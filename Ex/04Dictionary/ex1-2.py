
import os
pessoas= [{'nome':'João','idade':'18','cidade':'SP'}]

# Professor
# Atualização de Idade
# pessoa['idade'] = 31

# # Adicionando Profissão
# pessoa['profissao'] = 'Engenheiro'

# # Remoção de Elemento
# del pessoa['cidade']

def alterar_cadastro():
    for pessoa in pessoas:
        pessoa['nome'] = input('Altere o nome da pessoa:' )
        profissao = input('Adicione a profissão da pessoa: ')
        pessoa['profissao'] = profissao

def listar_cadastro():
    for pessoa in pessoas:
        pessoa.setdefault('profissao',' ')
        nome = pessoa['nome']
        profissao = pessoa['profissao'] 
        idade = pessoa['idade']
        cidade = pessoa['cidade']
        print(f' - {nome.ljust(20)} | {idade.ljust(20)} | {cidade.ljust(20)} | {profissao.ljust(20)}')
        #print(''&pessoa)
        
def main():
      os.system('cls')
      listar_cadastro()
      alterar_cadastro()
      listar_cadastro()
      deletar_item()

def deletar_item():
    for pessoa in pessoas:
        del pessoa['profissao']
    listar_cadastro()
    indice = 0
    pessoas.pop(indice)
    listar_cadastro()
    pessoas.append({'nome': 'João', 'idade': '32', 'cidade': 'MG'})
    listar_cadastro()

if __name__ == '__main__':
        main()
  

