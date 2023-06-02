import time
import os
import random
from tkinter import *
from tkinter import ttk

# Dicionário com as palavras e temas para cada dificuldade
palavras = {
    "fácil": {
        "animais": ["gato", "cachorro", "elefante", "leão", "tigre"],
        "frutas": ["maçã", "banana", "laranja", "uva", "morango"],
        "cores": ["azul", "vermelho", "verde", "amarelo", "roxo"]
    },
    "médio": {
        "países": ["brasil", "canadá", "japão", "alemanha", "méxico"],
        "carros": ["ferrari", "mercedes", "bmw", "audi", "lamborghini"],
        "filmes": ["avatar", "titanic", "vingadores", "matrix", "senhor dos anéis"]
    },
    "difícil": {
        "capitais": ["londres", "paris", "roma", "berlim", "tokyo"],
        "instrumentos": ["violino", "piano", "guitarra", "trompete", "flauta"],
        "profissões": ["médico", "advogado", "engenheiro", "professor", "dentista"]
    },
    "desafio": {
        "programação": ["python", "java", "csharp", "javascript", "ruby"],
        "esportes": ["futebol", "basquete", "tênis", "natação", "vôlei"],
        "bandas": ["coldplay", "maroon 5", "queen", "beatles", "u2"]
    }
}

# Dicionário com as pontuações por palavra para cada dificuldade
pontuacoes = {
    "fácil": 5,
    "médio": 10,
    "difícil": 15,
    "desafio": 25
}

# Função para exibir a tela inicial
def exibir_tela_inicial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1 - Novo jogo")
    print("2 - Maiores pontuadores")
    print("3 - Regras do jogo")
    print("4 - Créditos")

# Função para exibir as regras do jogo
def exibir_regras():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Regras do Jogo:")
    
    # Inserir as regras aqui

# Função para exibir os créditos
def exibir_creditos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Créditos:")
    # Inserir os créditos aqui

# Função para exibir o ranking
def exibir_maiores_pontuadores():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Maiores Pontuadores:")
    print()
    
    # Carregar os dados de pontuação dos usuários a partir do arquivo local
    if os.path.exists("users_score.txt"):
        with open("users_score.txt", "r") as file:
            scores = []
            for line in file:
                username, difficulty, score = line.strip().split(",")
                scores.append((username, difficulty, int(score)))
            
            # Ordenar as pontuações em ordem decrescente
            scores.sort(key=lambda x: x[2], reverse=True)
            
            # Exibir as pontuações
            for i, (username, difficulty, score) in enumerate(scores, start=1):
                print(f"{i}. {username} - Dificuldade: {difficulty} - Pontuação: {score}")
    else:
        print("Nenhum registro de pontuação encontrado.")

# Função para iniciar um novo jogo
def novo_jogo():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Escolha a dificuldade:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    print("4 - Desafio")
    
    # Obter a escolha da dificuldade do jogador
    dificuldade_escolhida = input("Digite o número da dificuldade: ")
    
    # Verificar se a escolha é válida
    while dificuldade_escolhida not in ["1", "2", "3", "4", "#"]:
        print("Escolha inválida. Por favor, escolha novamente.")
        dificuldade_escolhida = input("Digite o número da dificuldade: ")
    
    # Converter a escolha para o nome da dificuldade
    if dificuldade_escolhida == "1":
        dificuldade = "fácil"
    elif dificuldade_escolhida == "2":
        dificuldade = "médio"
    elif dificuldade_escolhida == "3":
        dificuldade = "difícil"
    elif dificuldade_escolhida == "4":
        dificuldade = "desafio"
    
    # Obter uma palavra aleatória da dificuldade escolhida
    tema = random.choice(list(palavras[dificuldade].keys()))
    palavra = random.choice(palavras[dificuldade][tema])
    
    # Exibir a palavra ocultada
    palavra_oculta = "-" * len(palavra)
    print(f"Tema: {tema}")
    print(f"Palavra: {palavra_oculta}")
    
    # Iniciar o cronômetro
    inicio = time.time()
    
    # Obter as tentativas do jogador
    tentativas = 0
    
    while True:
        letra = input("Digite uma letra: ")
        
        # Verificar se a letra já foi tentada
        if letra in palavra_oculta:
            print("Essa letra já foi tentada. Tente novamente.")
            continue
        
        # Atualizar a palavra oculta com as letras corretas
        nova_palavra_oculta = ""
        acertou_letra = False
        
        for i in range(len(palavra)):
            if palavra[i] == letra:
                nova_palavra_oculta += letra
                acertou_letra = True
            else:
                nova_palavra_oculta += palavra_oculta[i]
        
        if acertou_letra:
            print("Você acertou uma letra!")
            palavra_oculta = nova_palavra_oculta
        else:
            print("Você errou!")
        
        # Verificar se a palavra foi adivinhada corretamente
        if palavra_oculta == palavra:
            tempo_total = time.time() - inicio
            print(f"Parabéns! Você acertou a palavra '{palavra}' em {tentativas} tentativas.")
            print(f"Tempo total: {tempo_total:.2f} segundos.")
            
            # Adicionar a pontuação à lista
            scores.append((username, dificuldade, tentativas))
            
            # Salvar as pontuações atualizadas no arquivo
            with open("scores.txt", "w") as file:
                for score in scores:
                    file.write(f"{score[0]},{score[1]},{score[2]}\n")
            
            break
        
        # Verificar se o jogador atingiu o limite de tentativas
        if tentativas >= MAX_TENTATIVAS:
            print("Você atingiu o limite de tentativas!")
            print(f"A palavra era: {palavra}")
            break
        
        tentativas += 1

# Função para exibir o menu do jogo
def exibir_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("JOGO DA FORCA")
    print("1 - Novo Jogo")
    print("2 - Ver Ranking")
    print("3 - Regras do Jogo")
    print("4 - Créditos")
    print("5 - Sair")

# Função principal do jogo
def jogo_da_forca():
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            novo_jogo()
        elif opcao == "2":
            exibir_maiores_pontuadores()
        elif opcao == "3":
            exibir_regras()
        elif opcao == "4":
            exibir_creditos()
        elif opcao == "5":
            print("Obrigado por jogar! Até a próxima.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")
            time.sleep(1.5)

# Iniciar o jogo
jogo_da_forca()
