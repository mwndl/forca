# 7. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#       1. o produto do dobro do primeiro com metade do segundo .
#       2. a soma do triplo do primeiro com o terceiro.
#       3. o terceiro elevado ao cubo.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

resultado_a = (2 * numero1) * (numero2 / 2)
resultado_b = (3 * numero1) + numero_real
resultado_c = numero_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {resultado_a}")
print(f"A soma do triplo do primeiro com o terceiro é: {resultado_b}")
print(f"O terceiro elevado ao cubo é: {resultado_c}")
