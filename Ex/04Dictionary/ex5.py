import os

frase = "The real fox with her friend fox jump over the lazy fox"

dicionario = {'a': 1, 'b': 2, 'c': 3}

# Profesor
# frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
# contagem_palavras = {}
# palavras = frase.split()
# for palavra in palavras:
#     contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
# print(contagem_palavras)

def listar_dicionario():
    i = 0
    for chave,valor in dicionario.items():
        print(f'Chave : {chave} - valor  {valor}')

def main():
        os.system('cls')
        listar_dicionario()
        listar_frequencia(contar_palavras(frase))

def listar_frequencia(frequencia_palavras):
    for palavra, frequencia in frequencia_palavras.items():
        print(f"{palavra}: {frequencia}")
        
def contar_palavras(frase):

    palavras = frase.split()

    frequencia = {}

    for palavra in palavras:
        
        if palavra in frequencia:
            frequencia[palavra] += 1
       
        else:
            frequencia[palavra] = 1

    return frequencia

if __name__ == '__main__':
        main()

