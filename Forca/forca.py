import time
import random
import os

# Função para exibir a tela de entrada
def exibir_tela_entrada():

    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")


    print("    ********   *******   *******     ******      **    ")
    time.sleep(0.1)
    print("    /**/////   **/////** /**////**   **////**    ****   ")
    time.sleep(0.1)
    print("    /**       **     //**/**   /**  **    //    **//**  ")
    time.sleep(0.1)
    print("    /******* /**      /**/*******  /**         **  //** ")
    time.sleep(0.1)
    print("    /**////  /**      /**/**///**  /**        **********")
    time.sleep(0.1)
    print("    /**      //**     ** /**  //** //**    **/**//////**")
    time.sleep(0.1)
    print("    /**       //*******  /**   //** //****** /**     /**")
    time.sleep(0.1)
    print("    //         ///////   //     //   //////  //      // ")
    time.sleep(0.8)
    print("\n")


    # Simulação de animação de progresso
    print("Carregando jogo...")
    for _ in range(10):
        print(".", end="", flush=True)
        time.sleep(0.5)
    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    time.sleep(1)

# Função para exibir a tela de opções
def exibir_tela_opcoes():
    print("\n")
    print("1 - Novo Jogo")
    print("2 - Recordes")
    print("3 - Regras do Jogo")
    print("Pressione # para voltar")

# Função para exibir a tela de regras
def exibir_tela_regras():
    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n")
    print("Regras do Jogo:")
    print()
    print("- Como jogar:")
    print("     - A proposta do jogo é adivinhar a palavra secreta, revelando as letras uma a uma.")
    print("     - Você terá um número de seis (6) tentativas para acertar a palavra.")
    print("     - A cada letra correta, ela será revelada na palavra secreta.")
    print("     - Se conseguir adivinhar a palavra antes de esgotar as tentativas, você vence.")
    print("     - Caso contrário, você perde.")
    print()
    print("- Pontuações:")
    print("     - O jogo irá armazenar sua pontuação em um arquivo local para exibir os melhores jogadores")
    print("     - As pontuações são divididas com base na dificuldade selecionada. São elas:")
    print("         - Fácil: + 10 pontos por palavra correta")
    print("         - Médio: + 20 pontos por palavra correta")
    print("         - Difícil: + 30 pontos por palavra correta")
    print("         - Desafio: + 50 pontos por palavra correta")
    print()
    print("     - Cada jogador recebe 3 vidas (partidas), acerte o máximo possível e exiba seus pontos no placar de jogadores!")
    print()
    print("Pressione qualquer tecla para voltar")

# Função para exibir a tela de recordes
def exibir_tela_recordes():
    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')
    # Verifica se o arquivo de recordes existe
    if not os.path.exists("recordes.txt"):
        with open("recordes.txt", "w") as file:
            file.write("")

    with open("recordes.txt", "r") as file:
        recordes = file.readlines()

    if not recordes:
        print("Nenhum dado disponível :(")
    else:
        print("Recordes:")
        for recorde in recordes[:5]:
            nome, pontuacao = recorde.strip().split(",")
            print(f"{nome} - {pontuacao} pontos")

    print()
    print("Pressione # para voltar")

# Função para adicionar um novo recorde
def registrar_pontuacao(nome, pontuacao):
    with open("recordes.txt", "a") as arquivo:
        arquivo.write(f"{nome},{pontuacao}\n")
    exibir_tela_game_over(pontuacao)  # Exibe a tela de game over com o score do jogador


# Função para selecionar um tema e palavra aleatória de acordo com a dificuldade
def selecionar_palavra(dificuldade, tema):
    palavras = []
    temas = []

    if dificuldade == 1:
        palavras = palavras_facil
        temas = temas_facil
    elif dificuldade == 2:
        palavras = palavras_medio
        temas = temas_medio
    elif dificuldade == 3:
        palavras = palavras_dificil
        temas = temas_dificil
    elif dificuldade == 4:
        palavras = palavras_extremo
        temas = temas_extremo

    if tema.lower() == "aleatório":
        tema = random.choice(temas)

    index = temas.index(tema)
    palavra = random.choice(palavras[index])

    return tema, palavra

# Função principal do jogo
def jogar_forca():
    exibir_tela_entrada()
    vidas = 3
    score = 0  
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_tela_opcoes()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if vidas == 0:
                exibir_tela_game_over(score)  
                break

            if vidas < 3:
                jogar_novamente = input("Deseja jogar novamente com um novo jogo? (Y/N): ")
                if jogar_novamente.lower() != "y":
                    break

            if tentativas == 0:
                print("\nGame Over! A palavra secreta era: " + palavra)
                vidas -= 1  # Decrementa a quantidade de vidas quando o jogador perde uma partida
                input("Pressione qualquer tecla para continuar.")
                continue


            nome_usuario = input("Digite o nome de usuário (até 10 caracteres): ")
            nome_usuario = nome_usuario.upper() if len(nome_usuario) <= 10 else nome_usuario[:10].upper()

            confirmar = input("User: " + nome_usuario + ", confirma? (Y/N): ")
            if confirmar.lower() != "y":
                continue

            exibir_tela_entrada()


            # Limpa a tela
            os.system('cls' if os.name == 'nt' else 'clear')

            print("Selecione a dificuldade:")
            print("1 - Fácil (10pts)")
            print("2 - Médio (20pts)")
            print("3 - Difícil (30pts)")
            print("4 - Desafio (50pts)")
            dificuldade = int(input("Digite o número da dificuldade desejada: "))


            # Limpa a tela
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\nTemas disponíveis:")
            if dificuldade == 1:
                temas = temas_facil
            elif dificuldade == 2:
                temas = temas_medio
            elif dificuldade == 3:
                temas = temas_dificil
            elif dificuldade == 4:
                temas = temas_extremo

            print(f"1 - Aleatório")
            for i, tema in enumerate(temas, start=2):
                print(f"{i} - {tema}")

            tema_num = int(input("Digite o número do tema desejado ou '1' para um tema aleatório: "))
            tema = "aleatório" if tema_num == 1 else temas[tema_num - 2]

            tema, palavra = selecionar_palavra(dificuldade, tema)

            # Inicialização da lógica do jogo
            palavra_secreta = list(palavra.lower())
            letras_descobertas = []
            tentativas = 6
            acertos = 0
            letras_utilizadas = []

            for _ in palavra_secreta:
                letras_descobertas.append("_")

            print("\nTema: " + tema)
            print("Palavra: " + " ".join(letras_descobertas))

            while tentativas > 0:
                letra = input("\nDigite uma letra: ").lower()
                letra = letra.replace("ç", "c")  # Remover acentuação e "ç"

                if letra in letras_utilizadas:
                    print("Você já utilizou essa letra. Tente novamente.")
                    continue

                letras_utilizadas.append(letra)

                if letra in palavra_secreta:
                    indices = [i for i, x in enumerate(palavra_secreta) if x == letra]
                    for i in indices:
                        letras_descobertas[i] = letra
                    acertos += len(indices)
                else:
                    tentativas -= 1

                print("\nPalavra: " + " ".join(letras_descobertas))
                print("Tentativas restantes: " + str(tentativas))
                print("Letras utilizadas: " + ", ".join(letras_utilizadas))

                if acertos == len(palavra_secreta):
                    print("\nParabéns! Você venceu!")
                    pontuacao = calcular_pontuacao(dificuldade)
                    registrar_pontuacao(nome_usuario, pontuacao)
                    break

            if tentativas == 0:
                print("\nGame Over! A palavra secreta era: " + palavra)

            jogar_novamente = input("\nDeseja jogar novamente? (Y/N): ")
            if jogar_novamente.lower() != "y":
                break

        elif opcao == "2":
            exibir_recordes()

        elif opcao == "3":
            exibir_regras()

        elif opcao == "#":
            continue

        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)

# Função para calcular a pontuação com base na dificuldade
def calcular_pontuacao(dificuldade):
    if dificuldade == 1:
        return 10
    elif dificuldade == 2:
        return 20
    elif dificuldade == 3:
        return 30
    elif dificuldade == 4:
        return 50

# Função para exibir a tela de opções
def exibir_tela_opcoes():
    print("1 - Novo Jogo")
    print("2 - Recordes")
    print("3 - Regras do Jogo")

# Função para exibir os recordes
def exibir_recordes():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_tela_opcoes()
    print("\nRecordes:\n")

    try:
        with open("recordes.txt", "r") as arquivo:
            recordes = arquivo.readlines()
            if len(recordes) > 0:
                recordes = [recorde.strip().split(",") for recorde in recordes]
                recordes = sorted(recordes, key=lambda x: int(x[1]), reverse=True)
                for i, recorde in enumerate(recordes[:5], start=1):
                    print(f"{i}. {recorde[0]} - {recorde[1]} pontos")
            else:
                print("Nenhum dado disponível :(")
    except FileNotFoundError:
        print("Nenhum dado disponível :(")

    input("\nPressione qualquer tecla para voltar.")

# Função para exibir as regras do jogo
def exibir_regras():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_tela_opcoes()
    print("Regras do Jogo:")
    print()
    print("- Como jogar:")
    print("     - A proposta do jogo é adivinhar a palavra secreta, revelando as letras uma a uma.")
    print("     - Você terá um número de 6 tentativas de letra por palavra e 3 vidas gerais no jogo.")
    print("     - A cada letra correta, ela será revelada na palavra secreta.")
    print("     - Se conseguir adivinhar a palavra antes de esgotar as tentativas, você vence.")
    print("     - Caso contrário, você perde.")
    print("- Pontuações:")
    print("     - O jogo irá armazenar sua pontuação em um arquivo local para exibir os melhores jogadores")
    print("     - As pontuações são divididas com base na dificuldade selecionada. São elas:")
    print("         - Fácil: + 10 pontos por palavra correta")
    print("         - Médio: + 20 pontos por palavra correta")
    print("         - Difícil: + 30 pontos por palavra correta")
    print("         - Desafio: + 50 pontos por palavra correta")
    print()
    input("\nPressione qualquer tecla para voltar.")

# Função para registrar a pontuação do jogador
def registrar_pontuacao(nome, pontuacao):
    with open("recordes.txt", "a") as arquivo:
        arquivo.write(f"{nome},{pontuacao}\n")

# Função para exibir a tela de game over com score
def exibir_tela_game_over(score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    print("=== GAME OVER ===")
    print(f"Score: {score}")
    print("\n")
    input("Pressione qualquer tecla para voltar.")

# Listas de palavras e temas por dificuldade
palavras_facil = [
    ["abacaxi", "banana", "laranja", "limao", "uva"],
    ["cachorro", "gato", "coelho", "peixe", "papagaio"],
    ["brasil", "argentina", "chile", "colombia", "peru"]
]
temas_facil = ["Frutas", "Animais", "Países"]

palavras_medio = [
    ["computador", "teclado", "mouse", "monitor", "impressora"],
    ["carro", "bicicleta", "moto", "onibus", "caminhao"],
    ["amarelo", "azul", "verde", "vermelho", "roxo"]
]
temas_medio = ["Informática", "Veículos", "Cores"]

palavras_dificil = [
    ["eletroencefalograma", "anticonstitucionalissimamente", "otorrinolaringologista", "paralelepipedo", "desoxirribonucleico"],
    ["filantropo", "paradigma", "sublime", "efemero", "anacronismo"],
    ["meticuloso", "procrastinar", "inexoravel", "efervescente", "ininterrupto"]
]
temas_dificil = ["Palavras Grandes", "Palavras Difíceis", "Adjetivos"]

palavras_extremo = [
    ["hipopotomonstrosesquipedaliofobia", "pneumoultramicroscopicsilicovulcanoconiose", "criptozoologia", "parassimpaticomimético", "simiesco"],
    ["euforico", "gregario", "fascinio", "voraz", "adamantino"],
    ["probo", "perplexo", "idiossincrasia", "extemporaneo", "incongruente"]
]
temas_extremo = ["Palavras Enormes", "Palavras Raras", "Adjetivos Complexos"]

jogar_forca()