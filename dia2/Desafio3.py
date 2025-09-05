import math

class FiguraGeometrica:
    def area_circulo(self, raio):
        # Calcula e retorna a área do círculo
        return math.pi * math.pow(raio, 2)

    def area_triangulo(self, base, altura):
        # Calcula e retorna a área do triângulo
        return (base * altura) / 2

    def hipotenusa(self, cateto1, cateto2):
        # Calcula e retorna a hipotenusa do triângulo retângulo
        return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))

def menu():
    figura = FiguraGeometrica()

    while True:
        print("\nEscolha o cálculo que deseja realizar:")
        print("1 - Área do círculo")
        print("2 - Área do triângulo")
        print("3 - Hipotenusa do triângulo retângulo")
        print("0 - Sair")

        escolha = input("Digite a opção: ")

        if escolha == '1':
            raio = float(input("Digite o raio do círculo: "))
            resultado = figura.area_circulo(raio)  # Função retorna o resultado
            print(f"A área do círculo é: {resultado:.2f}")

        elif escolha == '2':
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            resultado = figura.area_triangulo(base, altura)  # Função retorna o resultado
            print(f"A área do triângulo é: {resultado:.2f}")

        elif escolha == '3':
            cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
            cateto2 = float(input("Digite o comprimento do segundo cateto: "))
            resultado = figura.hipotenusa(cateto1, cateto2)  # Função retorna o resultado
            print(f"A hipotenusa do triângulo retângulo é: {resultado:.2f}")

        elif escolha == '0':
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
