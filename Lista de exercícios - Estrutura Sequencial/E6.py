# 6. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

