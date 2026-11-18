x = 0
for i in range(1,5):

    n = float(input(f"Digite a °{i} nota do aluno:\n"))

    x = n + x

m = x/4


if m >= 7: 
    print(f"\nO aluno teve uma média de {m} e foi Aprovado!")
elif m >= 5:
    print(f"\nO aluno teve uma média de {m} e ficou de Recuperação!")
else:
    print(f"\nO aluno teve uma média de {m} e foi Reprovado!")