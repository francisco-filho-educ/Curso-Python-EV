class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.a = lado_a
        self.b = lado_b
    
    def muda_valores(self, novo_a, novo_b):
        self.a = novo_a
        self.b = novo_b
    
    def renorna_lados(self):
        print(f"Dimensões:\n{self.a}m² X {self.b}m²")

    def calcula_area(self):
        return self.a * self.b
