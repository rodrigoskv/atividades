import math
lista = [1,5,3,5,10,11,2,9,12,5]
sum = 0
multiple = 1
underMedia= 0
aboveMedia = 0
bigger = max(lista)
smaller = min(lista)

for i in range(0 , len(lista)):
    aux = lista[i]
    sum += aux
media = sum / len(lista)

for i in range(0 , len(lista)):
    aux = lista[i]
    multiple *= aux
mediaGeo = multiple ** (1/len(lista))

for i in range(0 , len(lista)):
    aux = lista[i]
    if aux < media:
        underMedia += 1

for i in range(0 , len(lista)):
    aux = lista[i]
    if aux > media:
        aboveMedia += 1

print("o maior é", bigger)
print("o menor é", smaller)
print(f"a média aritmética é {media: .2f}")
print(f"a média geográfica é {mediaGeo: .2f}")
print(aboveMedia, "ficaram acima da média")
print(underMedia, "ficaram abaixo da média")