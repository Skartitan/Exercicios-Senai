def areaT(b,a):
    area = b*a
    return area

while True:

    b = int(input("Digite a base do retângulo: "))
    a = int(input("Digite a altura do retângulo: "))

    print(f"A área do retângulo é de: {areaT(b,a):.2f}")
