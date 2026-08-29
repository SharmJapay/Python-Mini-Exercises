"""Different ways on how to convert a list to a string"""

import ast
import json


def main():
    """Start the program and run all steps in order."""

    # Create a string with words separated by space
    text = "The quick brown fox jumps over a lazy dog"

    # Method 1: Use of .split() string method
    converted_string1 = text.split()

    print(converted_string1)

    # Create a string with words separated by comma
    fruits = "apple, banana, cherry, durian"

    # Method 2: Use of .split() string method with specific separator
    converted_string2 = fruits.split(", ")

    print(converted_string2)

    # Method 3: Use of list() function to catch every character in string
    converted_string3 = list(text)

    print(converted_string3)

    # Method 4: Use of List Comprehension to filter characters (example: all letters only)
    converted_string4 = [char for char in text if char.isalpha()]

    print(converted_string4)

    # Create a string that is literally written as a list
    fruit_list = '["apple", "banana", "cherry", "durian"]'
    string_list = "[1, 2, 3, 'four']"

    # Method 5: Use of Evaluators (json.load)
    print(json.loads(fruit_list))

    # Method 6: Use of Evaluators (ast.literal_eval)
    print(ast.literal_eval(string_list))


if __name__ == "__main__":
    main()
