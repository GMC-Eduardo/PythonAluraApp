import os
def exibir_subtitulo(texto):    
    '''
    Esta função é responsável por exibir um subtitulo informado por na função.
    
    Ela limpa a tela e cria uma linha de asteriscos (*) com o tamanho do texto mais 4 caracteres.
    Em seguida, exibe a linha criada, o texto fornecido e novamente a linha criada, pulando uma linha ao final.
    
    Inputs:
        texto (str): O texto que será exibido como subtítulo.
    Outputs:
        Nenhum.
    '''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()