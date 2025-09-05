import math 

def calcular_piso(num):
    return math.floor(num)

def calcular_teto(num):
    return math.ceil(num)

def arrend_num(num):
    return round(num)

num = float(input("Digite um numero para arrendondamento: "))

piso = calcular_piso(num)
teto =  calcular_teto(num)
arrendondamento = arrend_num(num)

print(f"\nvalor sem arrendodamento: {num}")
print(f"piso: {piso}")
print(f"teto: {teto}")
print(f"arrendondado: {arrendondamento}")
  

