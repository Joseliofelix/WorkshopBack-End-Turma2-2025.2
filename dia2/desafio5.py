class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        return "O animal faz um som"
    
    def apresentar(self):
        return f"Meu nome é {self.nome} e eu tenho {self.idade} anos."

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def falar(self):
        return "Au au!"


def falar_do_animal(animal):
    print(animal.apresentar())
    print(animal.falar())

animais = [
    Gato("Mimi", 5),
    Cachorro("Rex", 3)
]

for animal in animais:
    falar_do_animal(animal)
