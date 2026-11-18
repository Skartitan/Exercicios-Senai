def M3(a,b,c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    else:
        return c

a = float(input("Digite o °1 número:"))
b = float(input("Digite o °2 número:"))
c = float(input("Digite o °3 número:"))

print(f"O maior número foi {M3(a,b,c):.0f}.")