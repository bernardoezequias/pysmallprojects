import random

random_number = random.randint(0, 15)
guess = int(input("Escolha um número de 0 a 15: "))

while True:
    if (guess == random_number):
        print("Acertou!")
        break
    elif (guess < random_number):
        print("Seu palpite é menor que o número gerado")
    else:
        print("Seu palpite é maior que o número gerado")

    guess = int(input("Tente mais uma vez: "))
