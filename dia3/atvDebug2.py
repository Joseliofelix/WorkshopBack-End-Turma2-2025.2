'''def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)
'''
# 1-Mensagem de erro: TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 2-Codigo corrigido:

def somar(a, b):
    try:
        b = int(b)
    except (ValueError, TypeError):
        raise ValueError("O segundo parâmetro deve ser um número ou uma string numérica.")
    return a + b

resultado = somar(10, "5")
print(resultado)
#
#
