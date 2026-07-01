def add():
    a = float(input("First number: "))
    b = float(input("second number: "))
    print("Result:", a + b)

def subtract():
    a = float(input("First number: "))
    b = float(input("second number: "))
    print("Result:", a - b)

def multiply():
    a = float(input("First number: "))
    b = float(input("second number: "))
    print("Result:", a * b)

def divide():
    a = float(input("First number: "))
    b = float(input("second number: "))
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)

