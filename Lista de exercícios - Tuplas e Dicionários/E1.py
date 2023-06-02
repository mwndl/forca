# 1. Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu
# primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como
# primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre cada informação armazenada em seu
# dicionário.

pessoa = {
    "primeiro_nome": "Marcos",
    "sobrenome": "Vinicius",
    "idade": 21,
    "cidade": "João Pessoa"
}

print("Informações sobre a pessoa:")
print(f"Primeiro nome: {pessoa['primeiro_nome']}")
print(f"Sobrenome: {pessoa['sobrenome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Cidade: {pessoa['cidade']}")