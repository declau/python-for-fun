import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 31)
total_de_tentativas = 0
pontos = 300

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if nivel == 1:
    total_de_tentativas = 6
elif nivel == 2:
    total_de_tentativas = 4
else:
    total_de_tentativas = 2

for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa {rodada} de {total_de_tentativas}")

    chute = int(input("Digite um número entre 1 e 30: "))
    print("Você digitou ", chute)

    if chute < 1 or chute > 30:
        print("Você deve digitar um número entre 1 e 30!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do jogo")