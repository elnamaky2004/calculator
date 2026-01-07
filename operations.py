def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def power(a,b):
    return a ** b
def root(a,b):
    if b == 0:
        return "Error: Zeroth root is undefined"
    return a ** (1/b)
def modulus(a,b):
    return a % b