"""Different ways on how to find factorial of given number"""


def factorial(number):
    """Returns the Factorial of a number"""
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def main():
    """Start the program and run all steps in order."""
    while True:
        try:
            number = int(input("Enter a single number: "))
            break

        except ValueError:  # Catches if the input cannot be converted to integer
            print("The input must be a number only (int or float)")

    print(
        "\nMethod 1 - Calculate using user defined 'factorial()' function with an argument 'number'\n"
    )

    if number < 0:
        print("Error: No factorials exists for negative numbers")
    elif number == 0:
        print("The factorial of zero is 1")
    else:
        print(f"The factorial of the {number} is {factorial(number)}")

    print("\n---------------------------------------------------- \n")
    print("Method 2 - Using For Loop Iteration\n")

    # Check if the input has factorials
    if number < 0:
        print("Error: No factorials exists for negative numbers")
    elif number == 0:
        print("The factorial of zero is 1")
    else:
        factorial_result = 1
        for i in range(1, number + 1):
            factorial_result = factorial_result * i
        print(f"The factorial of the {number} is {factorial_result}")


if __name__ == "__main__":
    main()
