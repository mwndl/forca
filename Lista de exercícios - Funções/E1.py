# 1. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros
# formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que
# é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto
# sobre vendas.

def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo_total = custo + imposto
    return custo_total

# Exemplo de uso da função
taxa = int(input("Digite a taxa: "))  
custo_item = int(input("Digite o custo antes do imposto: "))  

custo_final = somaImposto(taxa, custo_item)
print(f"O custo final do item, incluindo o imposto, é: R${custo_final:.2f}")
