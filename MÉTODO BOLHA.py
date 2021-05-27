# COLOCA O VETOR EM ORDEM CRESCENTE PELO MÉTODO DA BOLHA
import random

def criaVetor(n):
    vetor = [0] * n
    for i in range(n):
        vetor[i] = random.randint(0, 30)
    print(vetor)
    return vetor

def bolha(vetor):
    for k in range(len(vetor)):
        for i in range(len(vetor) - 1 - k):
            if vetor[i] > vetor[i + 1]:
                temp = vetor[i]
                vetor[i] = vetor[i + 1]
                vetor[i + 1] = temp
    return vetor

def main():
    n = 5
    vetor = criaVetor(n)
    print(bolha(vetor))

main()