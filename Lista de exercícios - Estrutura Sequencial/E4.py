# 4. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario = valor_hora * horas_trabalhadas
print(f"Seu salário no mês é: R${salario:.2f}")

