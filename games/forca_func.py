import random


def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    posicao = random.randrange(0, len(palavras))
    palavra_secreta = palavras[posicao].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print("Você Ganhou!!!!")


def imprime_mensagem_perdedor():
    print("Você Perdeu!!!!")