import forca_func as forca


def jogar():

    forca.mensagem_abertura()

    print("Qual o tipo de palavra?")
    print("(1) Nomes (2) Frutas")

    palavra = forca.defina_tipo_palavra()

    nome_arquivo = forca.escolhe_arquivo(palavra)

    palavra_secreta = forca.carrega_palavra_secreta(
        nome_arquivo=nome_arquivo, primeira_linha_valida=3
    )

    letras_acertadas = forca.inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            forca.marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            forca.desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        forca.imprime_mensagem_vencedor()
    else:
        forca.imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
