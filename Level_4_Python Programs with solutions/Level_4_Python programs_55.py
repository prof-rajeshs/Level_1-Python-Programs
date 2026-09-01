def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b, a % b


while True:
    command = input("Calc> ").strip()

    if command.lower() == "exit":
        print("Calculator exited.")
        break

    if command.lower() not in ["add", "sub", "mul", "div"]:
        print("Invalid command")
        continue

    a = input("Enter first number: ").strip()
    b = input("Enter second number: ").strip()

    # Check valid numbers
    if not a.isdigit() or not b.isdigit():
        print("Invalid number")
        continue

    # Check maximum 50 digits
    if len(a) > 50 or len(b) > 50:
        print("Number cannot exceed 50 digits")
        continue

    # Check leading zeros
    if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
        print("Leading zeros are not allowed")
        continue

    a = int(a)
    b = int(b)

    if command.lower() == "add":
        print("Result:", add(a, b))

    elif command.lower() == "sub":
        print("Result:", subtract(a, b))

    elif command.lower() == "mul":
        print("Result:", multiply(a, b))

    elif command.lower() == "div":
        if b == 0:
            print("Division by zero is not allowed")
        else:
            quotient, remainder = divide(a, b)
            print("Quotient:", quotient)
            print("Remainder:", remainder)