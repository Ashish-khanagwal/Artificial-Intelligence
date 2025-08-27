from typing import Dict, List, Tuple, Union

n: int = 5

name: str = "Ashish"


# def sum(a: int, b: int) -> int:
#     return a + b
#
#
# print(sum(5, 3))


def greet(name: str) -> str:
    print(f"Hello, {name}")


greet("Ashish")


# LIST
def total(numbers: List[int]) -> int:
    return sum(numbers)


print(total([1, 2, 3, 4, 5]))


# DICT
def records(data: Dict[str, int]) -> None:
    for k, v in data.items():
        print(f"{k} -> {v}")


records({"Ashish": 24, "Manish": 23})
