import math
from typing import List

def odd_pair(n: int):
    if n % 2 == 0:
        return "Par"
    else:
        return "Impar"

def negative_number(n: int):
    if n < 0:
        return "Numero negativo"
    else:
        return "Numero positivo"

def prime_num(n: int):
    if n == 1:
        return "Não é primo"
    for i in range(2, n):
        if n % i == 0: return "Não é primo"
    return "É primo"

def euclidean_distance(x1: float, x2: float, y1: float, y2: float):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def leap_year(year: int):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return "bissexto"
    else:
        return "não é bissexto"

def factorial(n: int):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def sequential_sum(numbers: List[int]):
    return sum(numbers)

def arithmetic(numbers: List[int]):
    return sum(numbers) / len(numbers)

def multiplication_table(numbers: List[int]):
    n = numbers[0]
    return [f"{n}x{i} = {(i * n)}" for i in range(1, 11)]

def fibonacci(limit: int):
    result = []
    a, b = 0, 1
    while a <= limit:
        result.append(a)
        a, b = b, a + b
    return result

def mmc(a: int, b: int):
    biggest = max(a, b)
    result: int
    while True:
        if biggest % a == 0 and biggest % b == 0:
            result = biggest
            break
        biggest += 1
    return result

def get_bigger(numbers: List[int]):
    return max(numbers)

def get_smaller(numbers: List[int]):
    return min(numbers)

def average(numbers: List[int]):
    aux = 0
    for n in numbers:
        aux += n
    return aux / len(numbers)

def geometric_mean(numbers: List[int]):
    aux = 1
    for n in numbers:
        aux *= n
    return aux ** (1 / len(numbers))

def under_average(numbers: List[int]):
    aux = 0
    underAverage = 0
    for i in range(0, len(numbers)):
        aux = numbers[i]
        if aux < average(numbers):
            underAverage += 1
    return underAverage

def above_average(numbers: List[int]):
    aux = 0
    aboveAverage = 0
    for i in range(0, len(numbers)):
        aux = numbers[i]
        if aux > average(numbers):
            aboveAverage += 1
    return aboveAverage

def median(numbers: List[int]):
    ordered = sorted(numbers)
    middle = len(ordered) // 2
    median = []

    if len(ordered) % 2 == 0:
        median.append((ordered[middle - 1] + ordered[middle]) / 2)
    else:
        median.append(ordered[middle])
    return median