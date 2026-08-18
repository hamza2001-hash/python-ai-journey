def add (a,b):
    return a + b

def subtract (a,b):
    return a - b

def multiply (a,b):
    return a * b    

def divide (a,b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))
input3 = input("Enter operation (+, -, *, /): ")

if input3 == "+":
    print(f"Result: {add(input1, input2)}")
elif input3 == "-":
    print(f"Result: {subtract(input1, input2)}")
elif input3 == "*":
    print(f"Result: {multiply(input1, input2)}")
elif input3 == "/":
    print(f"Result: {divide(input1, input2)}")
else:
    print("Invalid operation!")
