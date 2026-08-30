"""Different ways on how to convert a byte to a string"""

import codecs


def main():
    """Start the program and run all steps in order."""

    # Converting raw binary (bytes) to a string

    binary_data = b"Hello World!"

    # Method 1: Use of .decode() method

    string = binary_data.decode()

    print(string)

    ascii_string = binary_data.decode("ascii")

    print(ascii_string)

    # Method 2: Use of str() function

    string_text = str(binary_data, encoding="utf-8")

    print(string_text)

    # Method 3: Use of codecs

    codecs_string = codecs.decode(binary_data, "utf-8")

    print(codecs_string)


if __name__ == "__main__":
    main()
