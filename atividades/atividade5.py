ano = int(input("Informe um ano: "))

def anoBissexto(ano):
    if ano % 400 == 0 or (ano % 100 != 0 and ano % 4 == 0):
        return print("bissexto")
    else:
        return print("não é bissexto")

anoBissexto(ano)