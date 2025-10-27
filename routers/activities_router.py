from fastapi import APIRouter
from models.activities_model import *
from schema.activities_schema import *

router = APIRouter()

@router.get("/odd-pair", response_model=str)
def odd_pair_endpoint(n:int):
    return odd_pair(n)

@router.get("/negative-number", response_model=str)
def negative_number_endpoint(n:int):
    return negative_number(n)

@router.get("/prime-num", response_model=str)
def prime_num_endpoint(n:int):
    return prime_num(n)

@router.get("/euclidean-distance", response_model=float)
def euclidean_distance_endpoint(x1:float, x2:float, y1:float, y2:float):
    return euclidean_distance(x1, y1, x2, y2)

@router.get("/leap-year", response_model=str)
def leap_year_endpoint(year:int):
    return leap_year(year)

@router.get("/factorial", response_model=int)
def factorial_endpoint(n:int):
    return factorial(n)

@router.post("/sequential-sum", response_model=int)
def sequential_sum_endpoint(payload: NumbersIn):
    return sequential_sum(payload.numbers)

@router.post("/arithmetic-mean", response_model=int)
def arithmetic_endpoint(payload: NumbersIn):
    return arithmetic(payload.numbers)

@router.post("/multiplication-table", response_model=List[str])
def multiplication_table_endpoint(payload: NumbersIn):
    return multiplication_table(payload.numbers)

@router.post("/fibonacci", response_model=List[int])
def fibonacci_endpoint(limit:int):
    return fibonacci(limit)

@router.get("/mmc", response_model=int)
def mmc_endpoint(a:int, b:int):
    return mmc(a, b)

@router.post("/list/bigger", response_model=int)
def get_bigger_endpoint(payload:NumbersIn):
    return get_bigger(payload.numbers)

@router.post("/list/smaller", response_model=int)
def get_smaller_endpoint(payload: NumbersIn):
    return get_smaller(payload.numbers)

@router.post("/list/average", response_model=int)
def average_endpoint(payload: NumbersIn):
    return average(payload.numbers)

@router.post("/list/geometric-mean", response_model=float)
def geometric_mean_endpoint(payload: NumbersIn):
    return geometric_mean(payload.numbers)

@router.post("/list/under-average", response_model=int)
def under_average_endpoint(payload: NumbersIn):
    return under_average(payload.numbers)

@router.post("/list/above-average", response_model=int)
def above_average_endpoint(payload: NumbersIn):
    return above_average(payload.numbers)

@router.post("/list/median", response_model=List[float])
def median_endpoint(payload: NumbersIn):
    return median(payload.numbers)
