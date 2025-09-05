class Animal:
    def falar(self):
        return "O animal faz um som"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

animais = [Gato(), Cachorro()]
for animal in animais:
    print(animal.falar())
