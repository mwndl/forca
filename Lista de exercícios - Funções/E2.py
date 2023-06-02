# 2. Faça uma função que informe a quantidade de dígitos de uma determinada frase informada pelo usuário(a).

def contarDigitos(frase):
    digitos = 0
    for caractere in frase:
        if caractere.isdigit():
            digitos += 1
    return digitos

# Exemplo de uso da função
frase = input("Digite uma frase: ")
quantidade_caracteres = len(frase)
print(f"A frase '{frase}' possui {quantidade_caracteres} caracteres.")

