"""Different ways on how to convert a string to a number"""

from decimal import Decimal
from fractions import Fraction
import ast


def main():
    """Start the program and run all steps in order."""

    # Built-in Core Functions

    # Method 1: Use  of int(string) function
    number = "100"
    integer_value = int(number)

    print(integer_value)  # 100 (Integer)

    # Method 2: Use of int(string, base) function
    hex_num = int("1a", 16)
    bin_num = int("1010", 2)

    print(hex_num)  # 26 (Hexadecimal)
    print(bin_num)  # 10 (Binary)

    # Method 3: Use of float(string) function
    value1 = float("3.14")
    value2 = float("1e-3")

    print(value1)  # 3.14
    print(value2)  # 0.001 (Scientific notation)

    # Method 4: Use of complex(string) function
    complex_number = complex("3+4j")  # (3+4j)

    print(complex_number)

    # Standard Library Modules

    # Method 1: Use of decimal.Decimal(string)
    money = Decimal("10.99")

    print(money)  # 10.99

    # Method 2: Use of fractions.Fraction(string)
    fraction = Fraction("3/4")

    print(fraction)  # 3/4

    # Method 3: Use of ast.literal_eval()
    num = ast.literal_eval("123.45")

    print(num)  # 123.45 (float)


if __name__ == "__main__":
    main()
