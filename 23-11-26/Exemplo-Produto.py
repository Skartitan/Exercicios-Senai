class Produto:
    def _init_(self, nome, preço, estoque):
        self.nome = nome
        self.preço = preço
        self.estoque = estoque

    def exibir(self):
        print(f"produto: {self.nome}")
        print(f"preço: {self.preço}")
        print(f"estoque: {self.estoque}")
        print("-" * 80)

p1 = Produto("Arroz",5.99,30)
p2 = Produto("Macacarrão",8.5,80)

print(type(p1))
print(p1)
print(p1 == p2)

#FORMA EXTENSA DE CHAMAR

print(p1.nome)
print(p1.preço)
print(p1.estoque)

p1.exibir()