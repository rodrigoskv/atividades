a = int(input("primeiro num: "))
b = int(input("segundo num: "))
maior = max(a, b)
while (True):
    if maior % a == 0 and maior % b == 0:
        print(f"mmc: {maior}")
        break
    maior += 1