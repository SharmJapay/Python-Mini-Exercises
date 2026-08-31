"""Different ways on how to convert a number to a hex string"""


def main():
    """Start the program and run all steps in order."""

    number = 255

    # Method 1: Use of hex() function

    # Standard conversion
    print(hex(number))
    # Output: '0xff'

    # Stripping the '0x' prefix if needed
    print(hex(number)[2:])
    # Output: 'ff'

    # Method 2: Using f-Strings

    # Lowercase without '0x'
    print(f"{number:x}")
    # Output: 'ff'

    # Uppercase without '0x'
    print(f"{number:X}")
    # Output: 'FF'

    # Lowercase with '0x'
    print(f"{number:#x}")
    # Output: '0xff'

    # Pad with leading zeros to a width of 4 digits
    print(f"{number:04x}")
    # Output: '00ff'

    # Method 3: Using the format() Function

    print(format(number, "x"))
    # Output: 'ff' (lowercase)

    print(format(number, "X"))
    # Output: 'FF' (uppercase)

    print(format(number, "#x"))
    # Output: '0xff' (with prefix)

    print(format(number, "04x"))
    # Output: '00ff' (padded to 4 chars)

    # Method 4: Using String Formatting (% Operator)

    print("%x" % number)
    # Output: 'ff' (lowercase)

    print("%X" % number)
    # Output: 'FF' (uppercase)


if __name__ == "__main__":
    main()
