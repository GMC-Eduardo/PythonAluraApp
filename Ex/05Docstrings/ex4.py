
import ex10
def opcao_invalida():  
    '''
    Esta função é responsável por informar usuário que a opção é invalida.
    
    Ela utiliza a função voltar_menu_principal() para executar o processo de volta ao menu
    
    Inputs:
        Nenhum.
    Outputs:
        Nenhum.
    '''
    print('Opção invalida!\n')
    voltar_menu_principal()

    
def voltar_menu_principal():    
    '''
    Esta função é responsável por esperar o usuário digitar um tecla então volta ao menu principal.
    
    Ela utiliza a função main() voltar o menu inicial após uma tecla ser digitada

    Inputs:
        Nenhum.
    Outputs:
        Nenhum.
    '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    ex10.main()