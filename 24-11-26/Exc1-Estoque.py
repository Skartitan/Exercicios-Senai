class Produto:

    def __init__(self,nome,categoria,preço,estoque):
        self.nome = nome
        self.categoria = categoria
        self.preço = preço
        self.estoque = estoque

    def exibir(self):
        print(f"Produto: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço: {self.preço}")
        print(f"Estoque: {self.estoque}")
        print("=" * 70)

    def valor_total(self):
        total = self.preço * self.estoque
        print(f"O Preço total de estoque do {self.nome} é de R${total}")
              
    def aplicar_desconto(self,percentual):
        self.preço *= (1-percentual / 100)
        print(f"Desconto aplicado! Novo preço: R$ {self.preço}")

    def vender(self,quantidade):
        if quantidade > self.estoque:
            print("Estoque Insuficiente!")
        else:
            self.estoque -= quantidade
            print(f"Vendido {quantidade} X {self.nome}.Estoque restante: {self.estoque}")

    def repor_estoque(self,quantidade):
        self.estoque += quantidade
        print(f"Novo Estoque: {self.estoque}")

p1 = Produto("Cantinho do Vale","bebida",13.00,24)
p2 = Produto("Snake Venom","bebida",513.00,12)

p1.valor_total()

p1.exibir()
p2.exibir()

p1.aplicar_desconto(20)
p2.aplicar_desconto(20)

print("=" * 70)
p1.vender(24)
p2.vender(24)

print("=" * 70)
p1.repor_estoque(12)
p2.repor_estoque(24)