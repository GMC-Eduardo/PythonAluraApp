import os, ex9, ex2 , ex1

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}
                      ]

    
def main():
    '''
    Esta função é responsável por iniciar o programa.
    
    Ela limpa a tela, exibe o nome do programa e em seguida chama as funções para exibir as opções disponíveis
    e permitir que o usuário escolha uma ação a ser executada.
    
    Inputs:
        Nenhum.
    
    Outputs:
        Nenhum.
    '''
    os.system('cls')
    ex1.exibir_nome_do_programa()
    ex2.exibir_opcoes()
    ex9.escolher_opcoes()



if __name__ == '__main__':
        main()
  
