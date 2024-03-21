import os

# Solução correta

# usuario_correto = "alura"
# senha_correta = "alura123"

# usuario = input("Digite o nome de usuário: ")
# senha = input("Digite a senha: ")

# if usuario == usuario_correto and senha == senha_correta:
#     print("Login bem sucedido!")
# else:
#     print("Credenciais inválidas. Tente novamente.")


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

def login(nome,senha):
    
    nome_tentativa = input('Digite seu usuário: ')
    if nome_tentativa == nome:
        checa_senha(nome,senha)
    else:
        os.system('cls')
        print('Erro - Usuário errado! tente novamente')
        login(nome, senha)

def checa_senha(nome,senha):
    senha_tentativa = input('Digite sua senha: ')
    if senha == senha_tentativa:
        os.system('cls')
        print('Parabens logado!')
    else:
        os.system('cls')
        print('Erro - Senha errada! tente novamente')
        login(nome, senha)
def main():
    exibe_tela()
    nome = cadastra_nome()
    senha = cadastra_senha()
    print('Logando no usuário\n')
    login(nome,senha)

if __name__ == '__main__':
    main()