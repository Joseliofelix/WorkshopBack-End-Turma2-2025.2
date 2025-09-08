''' codigo 
def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  
    return f"Idade válida: {idade}"

idade = int(input("Digite sua idade: "))
print(validar_idade(idade))
'''
# 1- teste1:(abc) -> ValueError: invalid literal for int() with base 10: 'abc'
# teste2:(-1) -> ValueError: A idade deve estar entre 0 e 120 anos!
# 2 - O try tenta executar o código que pode causar erro.
# O except captura esse erro e imprime uma mensagem amigável para o usuário.
# 3 - Codigo modificado:
'''
def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
    return f"Idade válida: {idade}"

try:
    idade = int(input("Digite sua idade: "))
    print(validar_idade(idade))
except ValueError as e:
    print(f"Erro: {e}. Por favor, insira uma idade válida.")


