def greet(name):
    return f"Привет, {name}!"

def calculate_area(radius):
    return 3.14159 * radius * radius

def is_even(number):
    return number % 2 == 0

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

version = "1.0"
author = "Космический Программист"