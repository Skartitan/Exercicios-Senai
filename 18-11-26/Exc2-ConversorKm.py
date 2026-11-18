def KM(km):
    resultado = km * 0.6214
    return resultado

def MK(milhas):
    resultado = milhas / 0.6214
    return resultado

resultado = 0
while True:

    op = int(input("============================\n"
                    "1 - KM para Milhas\n"
                    "2 - Milhas para KM \n"
                    "Escolha qual conversor deseja:\n"))

    if op not in [1,2,3]:
        print("Digite uma opção Valida!")
        continue
    
    km = float(input("Digite a quatidade:"))

    if op == 1:
        resultado = KM(km)

    elif op == 2:
        resultado = MK(km)

    else:
        print("Digite uma opção valida!")
    break
if resultado != 0:
 print(f"{resultado:.2f}")