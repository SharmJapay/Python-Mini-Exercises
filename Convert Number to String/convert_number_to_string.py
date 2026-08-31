"""Different ways on how to convert a number to a string"""


def main():
    """Start the program and run all steps in order."""

    number = 542

    # Method 1: Use of str() function
    converted_string1 = str(number)

    print(converted_string1)
    # Output: "42"

    print(type(converted_string1))
    # Output: <class 'str'>

    # Method 2: Use of f-Strings
    pi_value = 3.14159
    converted_string2 = f"{pi_value}"

    print(converted_string2)
    # Output: "3.14159"

    # You can also format the number during conversion
    converted_string2 = f"{pi_value:.2f}"

    print(converted_string2)
    # Output: "3.14"

    # Method 3: Use of .format() Method
    number = 100
    converted_string3 = "{}".format(number)

    print(converted_string3)
    # Output: "100"

    # Method 4: Legacy % Formatting (String Interpolation)
    number = 7
    converted_string4 = "%d" % number

    print(converted_string4)
    # Output: "7"


if __name__ == "__main__":
    main()
