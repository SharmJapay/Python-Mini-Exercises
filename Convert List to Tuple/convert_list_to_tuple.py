"""Different ways on how to convert a list to a tuple"""


def main():
    """Start the program and run all steps in order."""

    # Create a list of mixed value instance
    mixed_list = ["Hi", 123, "Hello", 234, "Thank You", 345]

    # Method 1: Use of tuple() function
    converted_string1 = tuple(mixed_list)

    print(converted_string1)

    # Method 2: Use of * Asterisk to unpack list
    converted_string2 = (*mixed_list,)

    print(converted_string2)


if __name__ == "__main__":
    main()
