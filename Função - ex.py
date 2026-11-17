def saudar(nome):
        print(f"Olá, {nome}!")

saudar("Raissa")
saudar("Rian")

def estatisticas (nums):
    total = sum(nums)
    media = total / len(nums)
    return total, media

t, m = estatisticas([8,9,7])
print(f"total: {t}, Média: {m}")

def somar(a,b): return a + b
def subtrair(a,b): return a - b
def multiplicar(a,b): return a * b
def dividir(a,b):
      if b == 0: return "Erro!"
      return a / b

while True:
    op = input("Operação (+-*/0):")
    if op == "0": break
    a = float(input("Num 1: "))
    b = float(input("Num 2: "))

# chamar função conforme 'op'
    if op == "+": print(somar(a,b))
    elif op == "-": print(subtrair(a,b))
    elif op == "*": print(multiplicar(a,b))
    elif op == "/": print(dividir(a,b))
    else: print("Operação inválida!")                           