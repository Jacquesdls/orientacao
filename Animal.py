class Animal:
    def __init__(self, numero_de_patas: int):
        self.numero_de_patas = numero_de_patas
        
    def fazer_barulho(self):
        print("Eu sou um animal")
        
class Cachorro(Animal):
    def __init__(self, numero_de_patas: int, cor: str):
        super().__init__(numero_de_patas)
        self.cor = cor
        
    def fazer_barulho(self):
        print("AU AU AU !!!!")
    
        