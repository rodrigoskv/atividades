sum = 0
for i in range(1, 11):  # TODO: Podemos usar também range(10) ou range(0,10) que irá de 0 a 9, que abrange 10 números
    numero = int(input("informe um numero para soma: "))
    sum += numero

media = sum / 10
print(f"A resultado da media foi= {media}")
