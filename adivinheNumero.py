from random import randint

def cueRandonNumberPC(min, max):
    return randint(min, max)


def findNumber(rangeNumber):
    numberToFind = randint(1, rangeNumber)
    cueNumberUser = 0
    cueNumberPC = 0
    minCuePC = 1
    maxCuePC = rangeNumber
    while cueNumberUser != numberToFind and cueNumberPC != numberToFind:
        cueNumberUser = int(input("Digite um palpite para encontrar o número secreto: "))
        if cueNumberUser > numberToFind:
            print(f"\nOps, your number {cueNumberUser} is too high, try a smaller number\n")
        elif cueNumberUser < numberToFind:
            print(f"\nOps, your number {cueNumberUser} is too small, try a higher number\n")

        cueNumberPC = cueRandonNumberPC(minCuePC, maxCuePC)
        if cueNumberPC > numberToFind:
            print(f'PC entered the number {cueNumberPC}, that was too high\n\n')
            maxCuePC = cueNumberPC - 1
        elif cueNumberPC < numberToFind:
            print(f'PC entered the number {cueNumberPC}, that was too small\n\n')
            minCuePC = cueNumberPC + 1


    if cueNumberUser == numberToFind:
        print(f'\n\nParabéns Jogador! Você acertou, o número secreto era {numberToFind}')
    if cueNumberPC == numberToFind:
        print(f'\n\nParabéns Computador! Você acertou, o número secreto era {numberToFind}')


rangeNumber = int(input("Digite um numero de range: "))
findNumber(rangeNumber)
