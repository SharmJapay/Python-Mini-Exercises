"""Different ways on how to reverse a string"""


def main():
    """Start the program and run all steps in order."""

    user_input = input("Enter a string:")
    print(f"Original {user_input = }")

    # Method 1 - Using For Loop

    sanitized_string1 = ""
    for char in user_input:
        sanitized_string1 = char + sanitized_string1

    print("Reversed String:")
    print(sanitized_string1)

    # Method 2 - Using Slice Notation

    sanitized_string2 = user_input[::-1]

    print("Reversed String:")
    print(sanitized_string2)

    # Method 3 - Using list with .join() method

    reverse_chars = []
    for char in list(user_input):
        reverse_chars.insert(0, char)

    sanitized_string3 = "".join(reverse_chars)

    print("Reversed String:")
    print(sanitized_string3)

    # Method 4 - Using reversed() function with .join() method

    sanitized_string4 = "".join(reversed(user_input))

    print("Reversed String:")
    print(sanitized_string4)


if __name__ == "__main__":
    main()
