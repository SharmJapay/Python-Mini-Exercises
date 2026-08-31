"""Different ways on how to convert a string to a tuple"""

import ast
import json


def main():
    """Start the program and run all steps in order."""

    text1 = "Hello World!"
    text2 = "apple,banana,cherry"
    tuple_string = "(1, 2, 3)"
    json_string = '["one", "two", "three"]'

    # Method 1: Use of tuple() function
    result1 = tuple(text1)

    print(result1)
    # Output: ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!')

    # Method 2: Use of split() and tuple() functions
    result2 = tuple(text2.split(","))

    print(result2)
    # Output: ('apple', 'banana', 'cherry')

    # Method 3: Use of ast.literal_eval()
    result3 = ast.literal_eval(tuple_string)

    print(result3)
    # Output: (1, 2, 3)

    # Method 4: Trailing comma inside parentheses
    result4 = (text1,)

    # Method 5: Passing a list wrapper to tuple()
    result5 = tuple([text1])

    print(result4)
    # Output: ('Hello World!',)

    print(result5)
    # Output: ('Hello World!',)

    # Method: Use of json.loads() and tuple() functions
    result = tuple(json.loads(json_string))

    print(result)
    # Output: ('one', 'two', 'three')


if __name__ == "__main__":
    main()
