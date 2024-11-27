import config


def add(num1: int, num2: int) -> int:
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    return num1 * num2


print(add(1, 2))

API_URL = config.API_URL
print(API_URL)
print(config.DB_HOST)
