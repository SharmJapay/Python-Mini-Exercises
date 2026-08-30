"""Different ways on how to convert a byte to a string"""


def main():
    """Start the program and run all steps in order."""

    # Converting a binary text string to characters

    binary_string = "0100100001100101011011000110110001101111"  # "Hello" in binary

    # Method 1: Use of List Comprehension with int() & chr() functions, and .join() string method

    # Split binary into 8-bit pieces, convert binary bits to base-10 integer, convert to character, and join together
    string_text1 = "".join(
        chr(int(binary_string[i : i + 8], 2)) for i in range(0, len(binary_string), 8)
    )

    print(string_text1)  # Output: Hello

    # Method 2: Use of int.to_bytes() and .decode() methods

    # Determine the number of bytes required
    number_of_bytes = len(binary_string) // 8

    # Convert binary to base-10 integer
    integer_value = int(binary_string, 2)

    # Convert integer to bytes, then decode to normal text string
    string_text2 = integer_value.to_bytes(number_of_bytes, byteorder="big").decode()

    print(string_text2)  # Output: Hello

    # Method 3: Use of For Loop
    string_text3 = ""

    for i in range(0, len(binary_string), 8):
        binary_bits = binary_string[i : i + 8]  # Split binary into 8-bit pieces
        decimal = int(binary_bits, 2)  # Convert binary bits to base-10 integer
        string_text3 += chr(decimal)  # Convert to character and append

    print(string_text3)  # Output: Hello


if __name__ == "__main__":
    main()
