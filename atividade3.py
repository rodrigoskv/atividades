import math
num=int(input("Digite um numero: "))

def numPrimo(n):
    if n == 1:
        return print("Não é primo")
    for i in range (2, n):
        if n % i == 0: return print("Não é primo")
    return print("É primo")

numPrimo(num)