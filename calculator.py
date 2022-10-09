# This is Simple function based Calculator
def add(a, b):
    return a+b


def mult(a, b):
    return a*b


def div(a, b):
    if b == 0:
        return f"A number cannot divisible by zero"
    else:
        return a/b


def sub(a, b):
    return abs(a-b)


if __name__ == '__main__':
    print("Calculator\nPlease select operation do you want to perform\n\t1 for Subtraction"
          "\n\t2 for Addition\n\t3 for Multiplication\n\t4 for Division")
    operation = int(input("Please enter: "))
    a = float(input("Please enter your first number: "))
    b = float(input("Please enter your second number: "))
    if operation == 1:
        print(sub(a, b))
    elif operation == 2:
        print(add(a, b))
    elif operation == 3:
        print(mult(a, b))
    elif operation == 4:
        print(div(a, b))
    else:
        print("Entered option not valid")
