class Funcionario:
    def __init__(self,nome,salarioB):
        self.nome = nome
        self.salarioB = salarioB

class Gerente(Funcionario):
    def calcular_salario(self):
        Salario = self.salarioB * 1.20
        print(f"O Salario do Gerente {self.nome} é {Salario}")

class Estagiario(Funcionario):
    def calcular_salario(self):
        Salario = self.salarioB
        print(f"O Salario do Estagiario {self.nome} é {Salario}")

G1 = Gerente("Rian",100)
E1 = Estagiario("Raissa",100)

G1.calcular_salario()
E1.calcular_salario()