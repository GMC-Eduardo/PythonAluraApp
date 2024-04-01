
import os
numerosQuadrado = [{1:1},{2:4},{3:9},{4:16},{5:25}]
# Professor
#numeros_quadrados = {x: x**2 for x in range(1, 6)}
#print(numeros_quadrados)

def main():
    os.system('cls')
    listar_cadastro()

def listar_cadastro():
    i = 0
    for numero in numerosQuadrado:
        i+= 1
        print(f"Quadrado de {i} é {numero[i]}")

if __name__ == '__main__':
        main()