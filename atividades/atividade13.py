lista = [1, 5, 3, 5, 10, 11, 2, 9, 12, 5]
sum1 = 0  # TODO:  sum é o nome de uma função padrão do python, evitar usar esse nome
multiple = 1
underMedia = 0
aboveMedia = 0
bigger = max(lista)
smaller = min(lista)

for i in range(0, len(lista)):
    aux = lista[i]
    sum1 += aux
media = sum1 / len(lista)

for i in range(0, len(lista)):
    aux = lista[i]
    multiple *= aux
mediaGeo = multiple ** (1 / len(lista))

for i in range(0, len(lista)):
    aux = lista[i]
    if aux < media:
        underMedia += 1

for i in range(0, len(lista)):
    aux = lista[i]
    if aux > media:
        aboveMedia += 1

print("o maior é", bigger)
print("o menor é", smaller)
print(f"a média aritmética é {media: .2f}")
print(f"a média geográfica é {mediaGeo: .2f}")
print(aboveMedia, "ficaram acima da média")
print(underMedia, "ficaram abaixo da média")

# TODO: Podemos fazer assim também
list = [1, 5, 3, 5, 10, 11, 2, 9, 12, 5]
sum_total = sum(list)  # sum é uma função do python que realiza a soma de todos os valores
assistant = 1

for number in lista:
    assistant *= number

average = sum_total / len(lista)
geometric_media = assistant ** (1 / len(lista))

below_average = sum(1 for x in lista if x < average)
above_average = sum(1 for x in lista if x > average)
print('------------------------')
print("O maior é", max(lista))
print("O menor é", min(lista))
print(f"A média aritmética é {average:.2f}")
print(f"A média geométrica é {geometric_media:.2f}")
print(above_average, "ficaram acima da média")
print(below_average, "ficaram abaixo da média")
