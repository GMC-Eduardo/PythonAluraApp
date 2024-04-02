import ex5 , ex4
from ex10 import restaurantes
def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
        Inputs:
        - Nome do restaurante (str)
        - Categoria (str): Categoria do restaurante
        Output:
        - Adiciona um novo restaurante a lista de restaurantes
    '''
    ex5.exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastra: ')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dado_do_restaurante = {'nome': nome_do_restaurante,'categoria':categoria_restaurante,'ativo':False}
    restaurantes.append(dado_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    ex4.voltar_menu_principal()