import time
import os
import random

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
    }
}

# Dicionário com as pontuações por palavra para cada dificuldade
pontuacoes = {
    "fácil": 5,
    "médio": 10,
    "difícil": 15,
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
    print()
    print(" - O jogo da Forca consiste em adivinhar uma palavra, revelando suas letras.")
    print(" - O jogador possui 6 tentativas para adivinhar a palavra completa.")
    print(" - A pontuação é calculada com base na dificuldade escolhida e na quantidade de letras corretas adivinhadas.")
    print(" - Cada letra correta adiciona pontos à pontuação acumulada.")
    print(" - Ao atingir o limite de tentativas, o jogo termina.")
    print()
    input("\nPressione qualquer tecla para voltar para a tela inicial.")

# Função para exibir os créditos
def exibir_creditos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Créditos:")
    print()
    print("Desenvolvido por: Marcos Wiendl")
    print("Github: URL")
    print("Linkedin: URL")
    print("Data: [Data Atual]")
    input("\nPressione qualquer tecla para voltar para a tela inicial.")

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
                scores.append((username, int(score)))
            
            # Ordenar os usuários por pontuação em ordem decrescente
            scores.sort(key=lambda x: x[1], reverse=True)
            
            # Exibir os 5 usuários com maior pontuação
            for i, (username, score) in enumerate(scores[:5], start=1):
                print(f"{i}. {username} - Pontuação: {score}")
    else:
        print("Nenhum registro de pontuação encontrado.")
    print()
    input("Pressione qualquer tecla para voltar para a tela inicial.")

# Função para obter a entrada do usuário na tela inicial
def obter_opcao():
    opcao = input("Digite o número da opção desejada: ")
    return opcao

# Função para obter a dificuldade do jogo
def obter_dificuldade():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Escolha a dificuldade:")
    print("1 - Fácil (5 pontos por letra)")
    print("2 - Médio (10 pontos por letra)")
    print("3 - Difícil (15 pontos por letra)")
    dificuldade_num = int(input("Digite o número da dificuldade escolhida: "))

    dificuldades = list(palavras.keys())

    while dificuldade_num < 1 or dificuldade_num > len(dificuldades):
        print("Dificuldade inválida. Por favor, escolha uma das opções disponíveis.")
        time.sleep(2.0)
        dificuldade_num = int(input("Digite o número da dificuldade escolhida: "))

    return dificuldades[dificuldade_num - 1]

# Função para obter o tema do jogo
def obter_tema(dificuldade):
    os.system('cls' if os.name == 'nt' else 'clear')
    temas = list(palavras[dificuldade].keys())

    print("Escolha um tema:")
    for i, tema in enumerate(temas):
        print(f"{i + 1} - {tema.capitalize()}")

    print("0 - Escolher um tema aleatório")
    tema_num = int(input("Digite o número do tema desejado: "))

    while tema_num < 0 or tema_num > len(temas):
        print("Tema inválido. Por favor, escolha uma das opções disponíveis.")
        time.sleep(2.0)
        tema_num = int(input("Digite o número do tema desejado: "))

    if tema_num == 0:
        return random.choice(temas)
    else:
        return temas[tema_num - 1]

# Função para escolher uma palavra aleatória com base na dificuldade e no tema
def escolher_palavra(dificuldade, tema):
    palavra = random.choice(palavras[dificuldade][tema])
    return palavra

# Função para verificar se a palavra foi adivinhada
def verificar_palavra_adivinhada(palavra, letras_corretas):
    for letra in palavra:
        if letra not in letras_corretas:
            return False
    return True

def escolher_nova_palavra(dificuldade, tema, palavra_atual):
    palavras_disponiveis = palavras[dificuldade][tema]
    if not palavras_disponiveis:
        return ""
    palavras_disponiveis.remove(palavra_atual)
    palavra = random.choice(palavras_disponiveis)
    return palavra

# Função para verificar se a letra já foi selecionada anteriormente
def verificar_letra_selecionada(letra, letras_corretas, letras_incorretas):
    if letra in letras_corretas or letra in letras_incorretas:
        return True
    return False

# Verifica se o jogador chegou em 6 letras incorretas
def verificar_erro_palavra(letras_incorretas):
    if len(letras_incorretas) > 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nNão foi dessa vez, você não acertou a palavra.")
        print("Pontuação acumulada: " + str(pontuacao))
        time.sleep(2.0)
        return True
    return False

# Função principal do jogo
def jogar_forca():
    os.system('cls' if os.name == 'nt' else 'clear')
    global pontuacao  # Declarar a variável como global

    vidas_palavras = 0
    vidas_letras = 0
    pontuacao = 0
    letras_corretas = []
    letras_incorretas = []

    print("Bem-vindo ao jogo da Forca!")
    time.sleep(0.5)
    print("Iniciando partida...")
    time.sleep(2.0)

    dificuldade = obter_dificuldade()
    tema = obter_tema(dificuldade)
    palavra = escolher_palavra(dificuldade, tema)

    while vidas_palavras < 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        vidas_letras = 0

        if not palavra:
            palavra = escolher_nova_palavra(dificuldade, tema, palavra_atual)

        print("\nTema: " + tema.capitalize())
        print("Palavra: " + "".join([letra if letra in letras_corretas else "_" for letra in palavra]))
        print(f"Letras incorretas: " + " ".join(letras_incorretas))
        print(f"Vidas gastas: {vidas_palavras}/3 ")
        letra = input("Digite uma letra: ")

        if letra == "#":
            break

        if verificar_letra_selecionada(letra, letras_corretas, letras_incorretas):
            print("Essa já foi, hein? Tente outra letra.")
            time.sleep(1.5)
            continue

        if letra in palavra:
            print("Mandou bem! +" + str(pontuacoes[dificuldade]) + " pontos acumulados.")
            pontuacao += pontuacoes[dificuldade]
            time.sleep(1.5)
            letras_corretas.append(letra)
        else:
            print("Letra incorreta!")
            letras_incorretas.append(letra)
            vidas_letras += 1
            time.sleep(1.5)

            if vidas_letras == 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nNão foi dessa vez, você não acertou a palavra.")
                print("Pontuação acumulada: " + str(pontuacao))
                time.sleep(2.0)
                vidas_palavras += 1
                palavra = None
                letras_corretas = []
                letras_incorretas = []

                if vidas_palavras == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nGame Over! O jogo acabou para você.")
                    print("Pontuação total: " + str(pontuacao))
                    time.sleep(2.0)
                    break

        if verificar_palavra_adivinhada(palavra, letras_corretas):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nParabéns, você adivinhou a palavra! ")
            print("Pontuação acumulada: " + str(pontuacao))
            time.sleep(2.0)
            palavra_atual = palavra
            palavra = None
            letras_corretas = []
            letras_incorretas = []

        if verificar_erro_palavra(letras_incorretas):
            vidas_palavras += 1
            palavra_atual = palavra
            palavra = None
            letras_corretas = []
            letras_incorretas = []

            if vidas_palavras == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nGame Over!.")
                print(f"Pontuação total: {pontuacao}")
                time.sleep(2.0)
                break

    username = input("Digite seu username: ")

    # Salvar a pontuação do usuário em um arquivo local
    with open("users_score.txt", "a") as file:
        file.write(f"{username},{dificuldade},{pontuacao}\n")

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\nSeu jogo foi salvo corretamente, {username}")
    input("Pressione qualquer tecla para voltar para a tela inicial.")

# Loop principal do jogo
while True:
    exibir_tela_inicial()
    opcao = obter_opcao()

    if opcao == "1":
        jogar_forca()
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
        print("Opção inválida. Por favor, escolha uma das opções disponíveis.")
