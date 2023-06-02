# 9. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#       1. Para homens: (72.7*h) - 58
#       2. Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a sua altura em metros: "))
sexo = input("Digite 'M' para homem ou 'F' para mulher: ")

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Digite 'M' para homem ou 'F' para mulher.")
