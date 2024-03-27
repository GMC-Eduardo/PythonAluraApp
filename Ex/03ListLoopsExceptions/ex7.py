

def opcao_invalida():
    print('Lista de elementos inválida, impossivel somar!\n')
    main()

def media_lista(lista_de_elementos):
    soma = 0
    try:
        for numero in lista_de_elementos:
            soma += numero
            if (len(lista_de_elementos)==0):
                raise ZeroDivisionError('Não é possível dividir por zero!')
        media =  soma/len(lista_de_elementos)
        print(f'A média dos valores da lista é: {media}')

    except ZeroDivisionError as e:
        print("Erro:", e)
    except:
        opcao_invalida()
   
def main():
    lista_de_elementos = [4,2]
    media_lista(lista_de_elementos)
    #cadastra_numero()
    
if __name__ == '__main__':
    main()
    
#solução correta
#     lista_valores = [15, 20, 25, 30]
# soma_valores = 0

# try:
#     for valor in lista_valores:
#         soma_valores += valor
#     media = soma_valores / len(lista_valores)
#     print(f"Média dos valores: {media}")
# except ZeroDivisionError:
#     print("A lista está vazia, não é possível calcular a média.")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")
