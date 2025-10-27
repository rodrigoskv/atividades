import math

print("Digites os pontos de ")
x1=float(input("Digite o valor de x1: "))
x2=float(input("Digite o valor de x2 "))

print("Digites os pontos de y")
y1=float(input("Digite o valor de y1: ="))
y2=float(input("Digite o valor de y2 ="))

def distEuclediana():
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("A distância euclidiana é:", distEuclediana())
