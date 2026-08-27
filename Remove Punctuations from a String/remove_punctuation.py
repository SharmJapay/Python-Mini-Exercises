"""Different ways on how to remove punctuations from a string"""

import string


def main():
    """Start the program and run all steps in order."""

    punctuations_list = list(string.punctuation)
    user_input = input("Enter words separated by single space:")

    # Method 1 - Using List Comprehension with .join() method

    filtered_chars = [char for char in user_input if char not in punctuations_list]
    sanitized_string1 = "".join(filtered_chars)

    print("String without punctuations:")
    print(sanitized_string1)

    # Method 2 - Using For Loop Iteration

    sanitized_string2 = ""
    for char in user_input:
        if char not in punctuations_list:
            sanitized_string2 = sanitized_string2 + char

    print("String without punctuations:")
    print(sanitized_string2)

    # Method 3 - Using .translate() & str.maketrans() methods

    sanitized_string3 = user_input.translate(str.maketrans("", "", string.punctuation))

    print("String without punctuations:")
    print(sanitized_string3)


if __name__ == "__main__":
    main()
