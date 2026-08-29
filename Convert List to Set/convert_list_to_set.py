"""Different ways on how to convert a list to a set"""


def main():
    """Start the program and run all steps in order."""

    # Create a list of mixed value instances
    mixed_list = ["one", 1, 2, "two", "three", 3]

    # Method 1: Use of set() function
    converted_string1 = set(mixed_list)

    print(converted_string1)

    # Method 2: Use of * Asterish to unpack list
    converted_string2 = {*mixed_list}

    print(converted_string2)

    # Method 3: Use of Set Comprehension
    converted_string3 = {value for value in mixed_list}

    print(converted_string3)

    # Method 4: Use of For Loop and set() function
    converted_string4 = set()

    for value in mixed_list:
        converted_string4.add(value)

    print(converted_string4)


if __name__ == "__main__":
    main()
