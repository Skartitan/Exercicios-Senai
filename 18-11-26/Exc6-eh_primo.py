def eh_primo(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

n = int(input("Digite um número inteiro: "))
if eh_primo(n):
    print(f"O número {n} é um número primo!")
else:
    print(f"O número {n} não é um número primo!")

for i in range (1,101):
    if eh_primo(i):
        print(i)