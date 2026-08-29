"""Different ways on how to convert a list to a string"""


def main():
    """Start the program and run all steps in order."""

    # Create a list of values with same instances
    greeting_list = ["Good", "morning", "everyone"]

    # Method 1: Use of .join() method
    converted_string1 = " ".join(greeting_list)

    print(converted_string1)

    # Create a list with values that have mixed instances
    # NOTE: For the next methods, use str() to cast all values into string instance
    random_list = ["Welcome", "to", "this", "Python", "tutorial", "\u00a9", 2026]

    # Method 2: Use of For Loop
    converted_string2 = ""

    for word in random_list:
        converted_string2 = (
            converted_string2 + " " + str(word) if converted_string2 else str(word)
        )

    print(converted_string2)

    # Method 3: Use of List Comprehension with .join() method
    filtered_string = [str(word) for word in random_list]

    converted_string3 = " ".join(filtered_string)

    print(converted_string3)

    # Method 4: Use of map() function with .join() method
    converted_string1 = " ".join(map(str, random_list))

    print(converted_string1)


if __name__ == "__main__":
    main()
