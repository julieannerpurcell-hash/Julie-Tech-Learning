def calculator():
    print("Simple Calculator")
    a = float(input("First number: "))
    op = input("Operator (+, -, *, /): ")
    b = float(input("Second number: "))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b if b != 0 else "Error: divide by zero"
    else:
        result = "Unknown operator"

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()