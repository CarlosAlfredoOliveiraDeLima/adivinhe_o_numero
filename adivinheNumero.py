from random import randint

def cueRandonNumberPC(max):
    return randint(1, max)


def findNumber(rangeNumber):
    numberToFind = randint(1, rangeNumber)
    cueNumberUser = 0
    cueNumberPC = 0

    while cueNumberUser != rangeNumber and cueNumberPC != rangeNumber:
        cueNumberUser = int(input("Digite um palpite para encontrar o número secreto: "))
        print(cueNumberUser)
        cueNumberPC = cueRandonNumberPC(rangeNumber)
        print(cueNumberPC)

    if cueNumberUser == numberToFind:
        print(f'Parabéns Jogador! Você acertou, o número secreto era {numberToFind}')
    else:
        print(f'Parabéns Computador! Você acertou, o número secreto era {numberToFind}')


rangeNumber = int(input("Digite um numero de range: "))
findNumber(rangeNumber)
