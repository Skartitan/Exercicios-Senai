class Veiculo:

    def __init__(self,marca,velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max

    def mover(self):
        return "MOVE"

class Bicicleta(Veiculo):

    def __init__(self,marca,velocidade_max,num_marchas,):
        self.num_marchas = num_marchas
        super().__init__(marca,velocidade_max)
    
    def mover(self):
        print (f"A {self.marca} se movimenta com uma mão no guidon e a outra na calcinha numa velocidade de {self.velocidade_max}.")

    def marchas(self):
        print(f"A {self.marca} tem um total de {self.num_marchas} marchas.")

class Carro(Veiculo):

    def __init__(self,marca,velocidade_max,num_portas):
        self.num_portas = num_portas
        super().__init__(marca,velocidade_max)


    def mover(self):
        print (f"O {self.marca} faz VRUM VRUM numa velocidade maxima de {self.velocidade_max}.")

    def portas(self):
        print(f"O {self.marca} tem um total de {self.num_portas} portas.")


c1 = Carro("Ford Ak",300,4)
b1 = Bicicleta("Monark",1500,6)

print("=" * 80)
b1.mover()
b1.marchas()
print("=" * 80)
c1.mover()
c1.portas()
print("=" * 80)