"""Different ways on how to convert a list to a string"""


def main():
    """Start the program and run all steps in order."""

    # Create a list of string-only values
    greeting_list = ["Good", "morning", "everyone"]

    # Method 1: Use of .join() string method only (Best for String-Only Lists)
    converted_string1 = " ".join(greeting_list)

    print(converted_string1)

    # Create a list with values that have mixed instances
    random_list = ["Welcome", "to", "this", "Python", "tutorial", "\u00a9", 2026]

    # Method 2: Use of map() function with .join() string method (Best for Numeric/Mixed Lists)
    converted_string2 = " ".join(map(str, random_list))

    print(converted_string2)

    # Method 3: Use of List Comprehension with str() function and .join() string method
    converted_string3 = " ".join([str(word) for word in random_list])

    print(converted_string3)

    # Method 4: Use of For Loop and str() function
    converted_string4 = ""

    for word in random_list:
        converted_string4 += str(word) + " "

    print(converted_string4)


if __name__ == "__main__":
    main()
