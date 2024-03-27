import os

def exibir_nome_do_programa():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")
    
def exibir_opcoes():
    print('1. Cadastra restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair cadastro\n')

def finalizar_app():
    os.system('cls')
    # os.system('clear') no mac
    print('Finalizando o app\n')

def escolher_opcoes():
    try:    
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def opcao_invalida():
    print('Opção invalida!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def main():
 os.system('cls')
 exibir_nome_do_programa()
 exibir_opcoes()
 escolher_opcoes()


if __name__ == '__main__':
        main()
 