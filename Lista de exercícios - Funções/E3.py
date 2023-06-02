# 3. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por
#   exemplo: 127 -> 721.

def reversoNumero(numero):
    numero_str = str(numero)
    numero_reverso_str = numero_str[::-1]
    numero_reverso = int(numero_reverso_str)
    return numero_reverso

# Exemplo de uso da função
numero = int(input("Digite um número inteiro: "))
reverso = reversoNumero(numero)
print(f"O reverso do número {numero} é: {reverso}")
