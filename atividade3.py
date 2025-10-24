num = int(input("Digite um numero: "))


def numPrimo(n):
    if n == 1:  # TODO 1
        return print("Não é primo")
    for i in range(2, n):  # TODO 2
        if n % i == 0:
            return print("Não é primo")
    return print("É primo")


numPrimo(num)

# TODO 1: Números negativos não são primos
# TODO 2 : Poderiamos usar range(2, int(n**0.5) + 1) para reduzir o número de iterações, verificando apenas até a raiz quadrada do número. Isso melhora a eficiência do código.
