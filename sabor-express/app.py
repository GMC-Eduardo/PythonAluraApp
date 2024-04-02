import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}
                      ]


def exibir_nome_do_programa():
    '''Essa função é responsavel por exibir o titulo'''

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")
    
def exibir_opcoes():
    '''Essa função é responsavel por exibir opções'''
    print('1. Cadastra restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair cadastro\n')

def finalizar_app():
    '''Essa função é responsavel por finalizar o app'''
    exibir_subtitulo('Finalizando o app')

def listar_restaurantes():
    '''Essa função é responsavel por listar restaurantes'''
    exibir_subtitulo('Listando os restaurante')
    print(f'{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsavel por exibir o subtitulo'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def alternar_estado_restaurante():
    '''Essa função é responsavel por alternar estado do restaurante'''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativo com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'

    voltar_menu_principal()
def escolher_opcoes():
    '''
    Esta função é responsável por permitir ao usuário escolher entre várias opções de ação relacionadas a restaurantes.

    Inputs:
        - Opção (int): Um número inteiro representando a opção escolhida pelo usuário.

    Outputs:
        - None

    Raises:
        - ValueError: Se a entrada do usuário não puder ser convertida em um número inteiro.

    As opções disponíveis são:
        1. Cadastrar novo restaurante.
        2. Listar restaurantes.
        3. Alternar estado de um restaurante.
        4. Finalizar aplicativo.
    '''
    try:    
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
           cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
        Inputs:
        - Nome do restaurante
        - Categoria
        Output:
        - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastra: ')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dado_do_restaurante = {'nome': nome_do_restaurante,'categoria':categoria_restaurante,'ativo':False}
    restaurantes.append(dado_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

def opcao_invalida():
    '''Essa função é responsavel por exibir para o usuário que a opção é invalida'''
    print('Opção invalida!\n')
    voltar_menu_principal()

def main():
 os.system('cls')
 exibir_nome_do_programa()
 exibir_opcoes()
 escolher_opcoes()
 
def voltar_menu_principal():
    '''Essa função é responsavel por voltar para o menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

if __name__ == '__main__':
        main()
  
