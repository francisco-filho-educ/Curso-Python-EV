
class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}
    
    def cadastro_horas(self, mes, horas):
        if (mes not in self.horas):
            self.horas[mes]  = horas
    
    def cadastro_salario_hora(self, mes, valor):
        if (mes not in self.salario_hora):
            self.salario_hora[mes]  = valor

    
    def calcular_salario(self, mes):
        if (mes in self.horas) and (mes in self.salario_hora):
            return self.horas[mes] * self.salario_hora[mes]
        else:
            print("Dados insuficientes para calcular o salário do mês:", mes)
            return None
    
    def __repr__(self):
        return f"Funcionario: {self.nome}\nE-mail={self.email}\nHoras/mes{self.horas} / Salario/hora{self.salario_hora}"

#Exemplo de uso 