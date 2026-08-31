"""Different ways on how to convert a dictionary to a tuple"""

import itertools


def main():
    """Start the program and run all steps in order."""

    # Case 1: Converting Key-Value Pairs into a Tuple of Tuples

    my_dict = {"a": 1, "b": 2, "c": 3}

    # Method 1: Use of tuple() function and .items() method
    result1 = tuple(my_dict.items())

    print(result1)
    # Output: (('a', 1), ('b', 2), ('c', 3))

    # Method 2: Use of List/Tuple Comprehension
    result2 = tuple((k, v) for k, v in my_dict.items())

    print(result2)
    # Output: (('a', 1), ('b', 2), ('c', 3))

    # Method 3: Use of zip() function
    result3 = tuple(zip(my_dict.keys(), my_dict.values()))

    print(result3)
    # Output: (('a', 1), ('b', 2), ('c', 3))

    # Case 2: Converting ONLY Dictionary Keys into a Tuple

    # Method 1: Use of tuple() function
    result4 = tuple(my_dict)

    print(result4)
    # Output: ('a', 'b', 'c')

    # Method 5: Use of tuple() function with .keys() method

    result5 = tuple(my_dict.keys())

    print(result5)
    # Output: ('a', 'b', 'c')

    # Method 6: Use of Asterisk Unpacking (*dict,)
    result6 = (*my_dict,)

    print(result6)
    # Output: ('a', 'b', 'c')

    # Case 3: Converting ONLY Dictionary Values into a Tuple

    # Method 1: Using tuple() function with .values() method
    result7 = tuple(my_dict.values())

    print(result7)
    # Output: (1, 2, 3)

    # Case 4: Flattening a Dictionary into a Single Flat Tuple

    # Method 1: Using a Generator Expression inside tuple()
    result8 = tuple(item for pair in my_dict.items() for item in pair)

    print(result8)
    # Output: ('a', 1, 'b', 2, 'c', 3)

    # Method 2: Using itertools.chain
    result9 = tuple(itertools.chain.from_iterable(my_dict.items()))

    print(result9)
    # Output: ('a', 1, 'b', 2, 'c', 3)


if __name__ == "__main__":
    main()
