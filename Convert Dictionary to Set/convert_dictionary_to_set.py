"""Different ways on how to convert a dictionary to a list"""


def main():
    """Start the program and run all steps in order."""

    # Case 1: Extracting Dictionary Keys into a Set

    my_dict1 = {"a": 1, "b": 2, "c": 3}

    # Method 1: Use of the set() constructor (Most common & efficient)
    key_set1 = set(my_dict1)

    print(key_set1)
    # Output: {'a', 'b', 'c'}

    # Method 2: Use of dict.keys() explicitly
    key_set2 = set(my_dict1.keys())

    print(key_set2)
    # Output: {'a', 'b', 'c'}

    # Method 3: Use of Set Comprehension
    key_set3 = {k for k in my_dict1 if k != "b"}

    print(key_set3)
    # Output: {'a', 'c'}

    # Case 2. Extracting Dictionary Values into a Set

    my_dict2 = {"a": 1, "b": 2, "c": 1}

    # Method 1: Use of set() with dict.values() (Most efficient)
    value_set1 = set(my_dict2.values())

    print(value_set1)
    # Output: {1, 2}

    # Method 2: Use of Set Comprehension
    value_set2 = {v for v in my_dict2.values() if v > 1}

    print(value_set2)
    # Output: {2}

    # Case 3: Extracting Key-Value Pairs into a Set

    my_dict3 = {"a": 1, "b": 2}

    # Method 1: Use of set() with dict.items()
    item_set1 = set(my_dict3.items())

    print(item_set1)
    # Output: {('a', 1), ('b', 2)}

    # Method 2: Use of Set Comprehension
    item_set2 = {(v, k) for k, v in my_dict3.items()}

    print(item_set2)
    # Output: {(1, 'a'), (2, 'b')}


if __name__ == "__main__":
    main()
