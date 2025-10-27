from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import math
from typing import List

app = FastAPI()
router = APIRouter()

class NumbersIn(BaseModel):
    numbers:List[int]

@router.get("/odd-pair", response_model=str)
def odd_pair(n:int):
    if  n % 2 ==0:
        return "Par"
    else:
        return "Impar"

@router.get("/negative-number", response_model=str)
def negative_number(n:int):
    if n < 0:
        return "Numero negativo"
    else:
        return "Numero positivo"

@router.get("/prime-num", response_model=str)
def prime_num(n:int):
    if n == 1:
        return "Não é primo"
    for i in range (2, n):
        if n % i == 0: return "Não é primo"
    return "É primo"

@router.get("/euclidean-distance", response_model=float)
def euclidean_distance(x1:float, x2:float, y1:float, y2:float):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

@router.get("/leap-year", response_model=str)
def leap_year(year:int):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return "bissexto"
    else:
        return "não é bissexto"

@router.get("/factorial", response_model=int)
def factorial(n:int):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

@router.post("/sequential-sum", response_model=int)
def sequential_sum(payload: NumbersIn):
    return sum(payload.numbers)

@router.post("/arithmetic-mean", response_model=int)
def arithmetic(payload: NumbersIn):
    return sum(payload.numbers)/len(payload.numbers)

@router.post("/multiplication-table", response_model=List[str])
def multiplication_table(payload: NumbersIn):
    n = payload.numbers[0]
    return [f"{n}x{i} = {(i * n)}" for i in range(1, 11)]

@router.post("/fibonacci", response_model=List[int])
def fibonacci(limit:int):
    result = []
    a, b = 0, 1
    while a <= limit:
        result.append(a)
        a, b = b, a+b
    return result

@router.get("/mmc", response_model=int)
def mmc(a:int, b:int):
    biggest = max(a, b)
    result:int
    while True:
        if biggest % a == 0 and biggest % b == 0:
            result=(biggest)
            break
        biggest += 1
    return result

@router.post("/list/bigger", response_model=int)
def get_bigger(payload:NumbersIn):
    return max(payload.numbers)

@router.post("/list/smaller", response_model=int)
def get_smaller(payload: NumbersIn):
    return min(payload.numbers)

@router.post("/list/average", response_model=int)
def average(payload: NumbersIn):
    aux = 0
    for n in payload.numbers:
        aux+=n
    return aux / len(payload.numbers)

@router.post("/list/geometric-mean", response_model=float)
def geometric_mean(payload: NumbersIn):
    aux = 1
    for n in payload.numbers:
        aux *= n
    return aux ** (1 / len(payload.numbers))

@router.post("/list/under-average", response_model=int)
def under_average(payload: NumbersIn):
    aux = 0
    underAverage = 0
    for i in range(0, len(payload.numbers)):
        aux = payload.numbers[i]
        if aux < average(payload):
            underAverage += 1
    return underAverage

@router.post("/list/above-average", response_model=int)
def above_average(payload: NumbersIn):
    aux = 0
    aboveAverage= 0
    for i in range(0, len(payload.numbers)):
        aux = payload.numbers[i]
        if aux > average(payload):
            aboveAverage += 1
    return aboveAverage

@router.post("/list/median", response_model=List[float])
def median(payload: NumbersIn):
    ordered = sorted(payload.numbers)
    middle = len(ordered) // 2
    median = []

    if len(ordered) % 2 == 0:
        median.append((ordered[middle - 1] + ordered[middle]) / 2)
    else:
        median.append(ordered[middle])

    return median


app.include_router(router)