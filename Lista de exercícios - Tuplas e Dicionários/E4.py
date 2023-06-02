# 4. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []

for i in range(30):
    idade = int(input(f"Informe a idade do aluno {i+1}: "))
    altura = float(input(f"Informe a altura do aluno (centímetros){i+1}: "))
    idades.append(idade)
    alturas.append(altura)

media_alturas = sum(alturas) / len(alturas)
alunos = sum(1 for i in range(30) if idades[i] > 13 and alturas[i] < media_alturas)

print(f"O número de alunos com mais de 13 anos e altura inferior à média é: {alunos}")
