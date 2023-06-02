# 2. Use um dicionário para armazenar os números favoritos de algumas pessoas. Escolha cinco colegas, e
# pergunte quais seus números favoritos. Use seus nomes para serem as chaves de cada número
# favorito. Ao final, exiba o nome de cada pessoa e seu número favorito.

numeros_favoritos = {
    "Alice": 7,
    "Bob": 3,
    "Carol": 5,
    "David": 9,
    "Eve": 2
}

print("Números favoritos das pessoas:")
for pessoa, numero in numeros_favoritos.items():
    print(f"{pessoa}: {numero}")
