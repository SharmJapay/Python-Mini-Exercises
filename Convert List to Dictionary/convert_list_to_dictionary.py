"""Different ways on how to convert a byte to a string"""

from itertools import zip_longest
from collections import Counter


def main():
    """Start the program and run all steps in order."""

    # Case 1: Pairing Two Lists (Keys and Values)

    keys = ["user1", "user2", "user3"]
    keys1 = ["user1", "user2", "user3", "user4", "user5"]
    values = ["Anna", "Betty", "Cathy"]

    # Method 1: Use of dict() and zip() function
    users1 = dict(zip(keys, values))

    print(users1)

    # Method 2: Use of Dictionary Comprehension
    users2 = {keys: values for keys, values in zip(keys, values)}

    print(users2)

    # Method 3: Use of itertools.zip_longest (Handling Unequal Lengths)
    users3 = dict(zip_longest(keys1, values, fillvalue=None))

    print(users3)

    # Case 2: Converting a Single Flat List

    fruit_list = ["apple", "banana", "cherry"]
    flat_list = ["a", 1, "b", 2, "c", 3]
    key_list = ["user1", "user2", "user3"]

    # Method 1: Use of List Indices as Keys with dict() and enumerate() functions
    fruit_dict = dict(enumerate(fruit_list))

    print(fruit_dict)

    # Method 2: Chunking an Alternating List (Flat to Pairs) with dict() and zip() functions
    flat_dict = dict(zip(flat_list[0::2], flat_list[1::2]))

    print(flat_dict)

    # Method 3: Giving All Elements a Default Value (dict.fromkeys)
    users4 = dict.fromkeys(key_list, "")

    print(users4)

    # Case 3: Converting Structured Lists

    nested_list = [("a", 1), ("b", 2), ("c", 3)]
    numbers = [1, 2, 3]

    # Method 1: Converting a List of Tuples / Sublists
    nested_dict = dict(nested_list)

    print(nested_dict)

    # Method 2: Mapping with Dictionary Comprehension
    number_dict = {x: x**2 for x in numbers}

    print(number_dict)

    # Case 4: Grouping & Counting
    items = ["a", "b", "a", "c", "b", "a", "d", "e", "f", "d"]

    # Method: Use of Counter object
    counter_dict = dict(Counter(items))

    print(counter_dict)


if __name__ == "__main__":
    main()
