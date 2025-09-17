import math


def square(x):
    square = x**2
    return (square)


x = float(input())
result = square(x)
rounded = math.ceil(result)
print(rounded)
