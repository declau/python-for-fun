numero_secreto = 21

chute_str = input("Qual seu número: ")
print("Você digitou ", chute_str)

chute = int(chute_str)


acerto = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acerto:
    print("Você acertou!!!")
elif maior:
    print("Você errou, numero maior que o numero secreto")
else:
    print("Você errou, numero menor que o numero secreto")

print("Fim de jogo")
