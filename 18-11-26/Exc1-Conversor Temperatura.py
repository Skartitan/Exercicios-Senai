# C° para F°
def CF(temp):
    resultado = (temp * 1.8) + 32
    return resultado

# F° para C°
def FC(temp):
    resultado = (temp - 32) / 1.8
    return resultado

# C° para K°
def CK(temp):
    resultado = (temp + 273.15)
    return resultado

# K° para C°
def KC(temp):
    resultado = (temp - 273.15)
    return resultado

# F° para K°

def FK(temp):
    resultado = ((temp - 273.15) * 1.8 + 273.15)
    return resultado

# K° para F°
def KF(temp):
    resultado = ((temp - 32) * 1.8 + 32)
    return resultado

resultado = 0

while True:

    op = int(input("============================\n"
                "1 - Celsius\n"
                "2 - Fahrenheit\n"
                "3 - Kelvin\n" 
                "0 - Sair\n"
                "Escolha a Temperatura que deseja transformar:\n"
                "============================\n"))
    if op == 0:
        break

    if op not in [1,2,3]:
        print("Digite uma opção Valida!")
        continue
    
    temp = float(input("Digite os Graus:\n"))

    if op == 1:
       op2 = int(input("1 - Fahrenheit\n"
                       "2 - Kelvin\n" 
                       "Escolha o tipo para converter: \n"))
       if op2 == 1:
           resultado = CF(temp)
       elif op2 == 2:
           resultado = CK(temp)

    elif op == 2:
        op2 = int(input("1 - Celsius\n"
                        "2 - Kelvin\n" 
                         "Escolha a temperatura para converter: \n"))
        if op2 == 1:
           resultado = FC(temp)
        elif op2 == 2:
           resultado = FK(temp)

    elif op == 3:
        op2 = int(input("1 - Fahrenheit\n"
                        "2 - Celsius\n" 
                        "Escolha a temperatura para converter: \n"))

        if op2 == 1:
           resultado = KF(temp)
        elif op2 == 2:
           resultado = KC(temp)

        break

    break

if resultado != 0:
    print(resultado)