# 5. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = []

for i in range(5):
    numero = int(input(f"Informe o número {i+1}: "))
    numeros.append(numero)

print("Números informados:")
for numero in numeros:
    print(numero)
