import ex5,ex4
from ex10 import restaurantes

def alternar_estado_restaurante():
    '''
    Esta função é responsável por alternar o estado de ativação de um restaurante.
    
    Ela solicita ao usuário o nome do restaurante que deseja alterar o estado e altera
    o valor da chave 'ativo' para o oposto do valor atual na lista de restaurantes.
    
    Caso o restaurante não seja encontrado na lista, uma mensagem será exibida informando
    ao usuário que o restaurante não foi encontrado.
    
    Inputs:
        Nenhum.
    
    Outputs:
        Nenhum.
    '''
    ex5.exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativo com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
    ex4.voltar_menu_principal()