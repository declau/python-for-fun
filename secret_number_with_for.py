numero_secreto = 21
total_tentativas = 3

for tentativa in range(1, total_tentativas + 1):

    print(f"Tentativa {tentativa} de {total_tentativas}")

    chute_str = input("Qual seu número: ")
    print("Você digitou ", chute_str)

    chute = int(chute_str)

    acerto = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acerto:
        print("Você acertou!!!")
        break
    elif maior:
        print("Você errou, numero maior que o numero secreto")
    else:
        print("Você errou, numero menor que o numero secreto")
    # total_tentativas = total_tentativas - 1
print("Fim de jogo")
