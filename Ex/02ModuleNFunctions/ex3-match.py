import os

def exibe_tela():
    print('CADASTRO DE USUÁRIO!')

def cadastra_nome():
    nome = input('Digite seu usuário para cadastrar: ')
    os.system('cls')
    return nome

def cadastra_senha():
    senha = input('Digite sua senha para cadastrar: ')
    os.system('cls')
    return senha

def login(nome, senha):
    nome_tentativa = input('Digite seu usuário: ')
    senha_tentativa = input('Digite sua senha: ')
    checa_nome(nome, senha,nome_tentativa, senha_tentativa)

def checa_nome(nome, senha,nome_tentativa, senha_tentativa):  
    match nome_tentativa:
        case n if nome == nome_tentativa:
            checa_senha(nome,senha,senha_tentativa)
        case _:
            os.system('cls')
            print('Erro - Usuário errado! Tente novamente (ಥ﹏ಥ)')
            login(nome, senha)

def checa_senha(nome,senha,senha_tentativa):  
    match senha_tentativa:
        case n if senha == senha_tentativa:
            os.system('cls')
            print('Parabéns, logado! (´∀`)♡')
        case _:
            os.system('cls')
            print('Erro - Senha errada! Tente novamente (｡•́︿•̀｡)')
            login(nome, senha)

def main():
    exibe_tela()
    nome = cadastra_nome()
    senha = cadastra_senha()
    print('Logando no usuário\n')
    login(nome, senha)

if __name__ == '__main__':
    main()
