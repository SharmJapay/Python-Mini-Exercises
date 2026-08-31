"""Different ways on how to convert a hex string into a number"""

import ast
import struct


def main():
    """Start the program and run all steps in order."""

    hex_string1 = "1A3F"

    # If you are writing the hexadecimal number directly in your code, prefix it with 0x or 0X.
    hex_string2 = "0x1A3F"

    # Method 1: Use of int() function (Works with or without the '0x' prefix)
    decimal1 = int(hex_string1, 16)
    decimal2 = int(hex_string2, 16)

    print(decimal1)  # Output: 6719
    print(decimal2)  # Output: 6719

    # Method 2: Use of ast.literal_eval (Works with the '0x' prefix only)
    decimal3 = ast.literal_eval(hex_string2)

    print(decimal3)  # Output: 6719

    # Method 3: Use of struct.unpack (Binary/Bytes Unpacking) (Works without the '0x' prefix only)

    # Convert hex string to a bytes object
    byte_data = bytes.fromhex(hex_string1)

    # Unpack as a 2-byte unsigned short (big-endian '>')
    decimal4 = struct.unpack(">H", byte_data)[0]

    print(decimal4)  # Output: 6719

    # Method 4: Use of For Loop

    hex_digits = "0123456789abcdef"
    decimal_val = 0

    # Convert letters to lowercase
    hex_str = "1A3F".lower()

    # Loop through each character and calculate its positional value
    for char in hex_str:
        decimal_val = decimal_val * 16 + hex_digits.index(char)

    print(decimal_val)  # Output: 6719


if __name__ == "__main__":
    main()
