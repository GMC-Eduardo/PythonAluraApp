import ex5,ex4
from ex10 import restaurantes

def listar_restaurantes():
    '''
    Esta função é responsável por listar os restaurantes.
    
    Ela exibe no console o nome a categoria e o status separados por 23 e 20 espaços logo após um pipeline (|) 
    
    Inputs:
        Nenhum.
    
    Outputs:
        Nenhum.
    '''
    ex5.exibir_subtitulo('Listando os restaurante')
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    ex4.voltar_menu_principal()