class Zoologico:
 def __init__(self):
    self.animais = []
  
 def adicionar_animal(self,animal):
    self.animais.append(Animal)
  
 def listar_animais(self):
    return[f"{a.apresentar()} faz:{a.falar()}"for a in self.animais]
  
 def filtrar_por_tipo(self,tipo):
    return [a for a in self.animais if isinstance(a, tipo)]