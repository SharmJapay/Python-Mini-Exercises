"""Different ways on how to convert a tuple to a dictionary"""

from collections import defaultdict


def main():
    """Start the program and run all steps in order."""

    # Case 1: Nested Tuples (Key-Value Pairs)

    data_tuple = (("Apple", 1), ("Banana", 2), ("Cherry", 3))

    # Method 1: Use of the Built-in dict() Constructor
    result1 = dict(data_tuple)

    print(result1)
    # Output: {'Apple': 1, 'Banana': 2, 'Cherry': 3}

    # Method 2: Use of Dictionary Comprehension
    result2 = {key.lower(): value for key, value in data_tuple}

    print(result2)
    # Output: {'apple': 1, 'banana': 2, 'cherry': 3}

    # Method 3: Use of For Loop
    result3 = {}

    for key, value in data_tuple:
        if value > 1:
            result3[key] = value

    print(result3)
    # Output: {'Banana': 2, 'Cherry': 3}

    # Case 2: Two Separate Tuples (Keys and Values)

    keys_tuple = ("name", "age", "role")
    values_tuple = ("Alice", 28, "Engineer")

    # Method 1: Combining dict() with zip() functions

    result4 = dict(zip(keys_tuple, values_tuple))

    print(result4)
    # Output: {'name': 'Alice', 'age': 28, 'role': 'Engineer'}

    # Case 3: Flat Tuple with Alternating Elements

    flat_tuple = ("a", 1, "b", 2, "c", 3)

    # Method 1: Pairing Slices with zip()

    result5 = dict(zip(flat_tuple[0::2], flat_tuple[1::2]))

    print(result5)
    # Output: {'a': 1, 'b': 2, 'c': 3}

    # Method 2: Use of iter() and zip()

    # Create an iterator instance
    it = iter(flat_tuple)

    # zip consumes two elements from the iterator at each iteration step
    result6 = dict(zip(it, it))

    print(result6)
    # Output: {'a': 1, 'b': 2, 'c': 3}

    # Case 4: Tuples with Duplicate Keys

    # Method 1: Use of collections.defaultdict

    duplicate_tuple = (("A", 10), ("B", 20), ("A", 30))
    result7 = defaultdict(list)

    for key, value in duplicate_tuple:
        result7[key].append(value)

    print(dict(result7))
    # Output: {'A': [10, 30], 'B': [20]}


if __name__ == "__main__":
    main()
