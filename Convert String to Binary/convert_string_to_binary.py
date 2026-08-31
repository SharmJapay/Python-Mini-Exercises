"""Different ways on how to convert a string to a binary"""


def main():
    """Start the program and run all steps in order."""

    # Case 1: Generating a 1 and 0 String

    text = "Hello World"

    # Method 1: Use of f-Strings
    binary_string1 = " ".join(f"{ord(char):08b}" for char in text)

    print(binary_string1)

    # Method 2: Use of format() function
    binary_string2 = " ".join(format(ord(char), "08b") for char in text)

    print(binary_string2)

    # Method 3: Use of bin() with String Slicing and zfill()
    binary_string3 = " ".join(bin(ord(char))[2:].zfill(8) for char in text)

    print(binary_string3)

    # Case 2: Converting String to Machine Binary (bytes Object)

    # Method 1: Use of .encode() Method
    binary_bytest1 = text.encode("utf-8")

    print(binary_bytest1)
    print(list(binary_bytest1))

    # Method 2: Use of bytes() Constructor
    binary_bytest2 = bytes(text, "utf-8")

    print(binary_bytest2)

    # Method 3: Use of bytearray() (For Mutable Binary Data)
    binary_bytest3 = bytearray(text, "utf-8")

    print(binary_bytest3)


if __name__ == "__main__":
    main()
