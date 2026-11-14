
def main():
    print("Hello, it's test calculator for dont forget based python work compiler")

    while True:

        print("Choose what function you want to do?"
              "\n1. Add first number with second number"
              "\n2. Minus first number with second number"
              "\n3. Multiple first number with second number"
              "\n4. Divide first number with second number"
              "\n5. Exit the program")

        choose = int(input("Input number of operation you want to do: "))

        if choose in ("1", "1."):
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            plus(a, b)

        elif choose in ("2", "2."):
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            minus(a, b)
        elif choose in ("3", "3."):
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            multiple(a, b)
        elif choose in ("4", "4."):
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            divide(a, b)
        elif choose in ("5", "5."):
            break


def plus(a, b):
    result = a + b
    print(f"The result of operation: {result}")
    return

def minus(a, b):
    result = a - b
    print(f"The result of operation: {result}")
    return

def multiple(a, b):
    result = a * b
    print(f"The result of operation: {result}")
    return

def divide(a, b):
    result = a / b
    print(f"The result of operation: {result}")
    return

if __name__ == "__main__":
    main()