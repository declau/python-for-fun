import forca_func as forca


def jogar():

    forca.mensagem_abertura()

    palavra_secreta = forca.carrega_palavra_secreta()

    letras_acertadas = forca.inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = len(letras_acertadas)

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            forca.marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros = erros - 1
            print(f"Ops, você errou! Faltam {erros}")

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        forca.imprime_mensagem_vencedor()
    else:
        forca.imprime_mensagem_perdedor()

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
