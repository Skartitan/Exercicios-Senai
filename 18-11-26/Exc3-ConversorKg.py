def KL(kg):
    resultado = kg * 2.2046
    return resultado

def LK(libras):
    resultado = libras / 2.2046
    return resultado

resultado = 0
while True:

    op = int(input("============================\n"
                    "1 - KG para Libras\n"
                    "2 - Libras para KG \n"
                    "0 - Sair\n"
                    "Escolha qual conversor deseja:\n"))
    if op == 0:
        break

    elif op not in [1,2,3]:
        print("Digite uma opção Valida!")
        continue

    peso = float(input("Digite o peso: "))

    if op == 1:
        resultado = KL(peso)

    elif op == 2:
        resultado = LK(peso)
    break

if resultado != 0:
    print(f"{resultado:.2f}")