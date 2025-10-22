n = int(input("digite um número: "))

def funcaoFatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
        print(fat)

funcaoFatorial(n)