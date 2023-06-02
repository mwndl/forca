# 3. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de
# cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []
alunos_aprovados = 0

for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input(f"Informe a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)
    if media >= 7.0:
        alunos_aprovados += 1

print(f"O número de alunos com média maior ou igual a 7.0 é: {alunos_aprovados}")
