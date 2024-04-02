import ex3,ex4,ex8,ex7,ex6
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
            ex6.cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            ex7.listar_restaurantes()
        elif opcao_escolhida == 3:
            ex8.alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            ex3.finalizar_app()
        else:
            ex4.opcao_invalida()
    except:
        ex4.opcao_invalida()