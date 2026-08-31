"""Different ways on how to convert a dictionary to a list"""

import itertools


def main():
    """Start the program and run all steps in order."""

    # Case 1. Extracting Only the Keys

    my_dict = {"a": 1, "b": 2, "c": 3}

    # Method 1: Use of the list() constructor directly
    result1 = list(my_dict)

    print(result1)
    # Output: ['a', 'b', 'c']

    # Method 2: Use of .keys() methods
    result2 = list(my_dict.keys())

    print(result2)
    # Output: ['a', 'b', 'c']

    # Method 3: Use of List Comprehension
    result3 = [key for key in my_dict]

    print(result3)
    # Output: ['a', 'b', 'c']

    # Case 2: Extracting Only the Values

    # Method 1: Use of .values() with list()
    result4 = list(my_dict.values())

    print(result4)
    # Output: ['1', '2', '3']

    # Method 2: Use of List Comprehension
    result5 = [val for val in my_dict.values()]

    print(result5)
    # Output: ['1', '2', '3']

    # Case 3: Extracting Both Keys and Values (List of Tuples)

    # Method 1: Use of .items() with list()
    result6 = list(my_dict.items())

    print(result6)
    # Output: [('a', 1), ('b', 2), ('c', 3)]

    # Method 2: Use of List Comprehension
    result7 = [(k, v) for k, v in my_dict.items()]

    print(result7)
    # Output: [('a', 1), ('b', 2), ('c', 3)]

    # Case 4: Extracting Both Keys and Values (Flattened List)

    # Method 1: Use of List Comprehension with dual loops:
    result8 = [item for pair in my_dict.items() for item in pair]

    print(result8)
    # Output: ['a', 1, 'b', 2, 'c', 3]

    # Method 2: Use of itertools.chain
    result9 = list(itertools.chain(*my_dict.items()))

    print(result9)
    # Output: ['a', 1, 'b', 2, 'c', 3]


if __name__ == "__main__":
    main()
