import random

print("*************************************")
print("Seja bem vindo ao jogo de Adivinhação")
print("*************************************")
numero_secreto = random.randrange(1, 31)
total_tentativas = 0

print("***Qual nível de dificuldade?***")
print("(1) - Fácil")
print("(2) - Médio")
print("(3) - Difícil")

nivel = int(input("Defina o Nível: "))

if nivel == 1:
    total_tentativas = 6
elif nivel == 2:
    total_tentativas == 4
else:
    total_tentativas == 2

for tentativa in range(1, total_tentativas + 1):

    print(f"Tentativa {tentativa} de {total_tentativas}")

    chute_str = input("Digite um número entre 1 e 30: ")
    print("Você digitou ", chute_str)

    chute = int(chute_str)
    if chute < 1 or chute > 30:
        print("Você deve digitar um número entre 1 e 30!")
        continue

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
