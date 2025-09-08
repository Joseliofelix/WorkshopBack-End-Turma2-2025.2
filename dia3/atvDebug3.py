''' Codigo:

numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])

'''
#1 - teste: (4) -> IndexError: list index out of range
#   teste: (ab) -> ValueError: invalid literal for int() with base 10: 'ab'
#2 - Codigo corrigido:
'''
numeros = [10, 20, 30, 40]
tentativas = 0
max_tentativas = 0

while tentativas < max_tentativas:
    entrada = input("Digite um índice para acessar a lista: ")
    try:
        indice = int(entrada)
        print(numeros[indice])
        break  
    except ValueError:
        print("Erro: por favor, digite um número inteiro.")
        tentativas += 1
    except IndexError:
        print("Erro: índice fora do intervalo da lista.")
        tentativas += 1

if tentativas == max_tentativas:
    print("Número máximo de tentativas inválidas atingido.")

'''
#
