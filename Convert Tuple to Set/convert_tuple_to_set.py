"""Different ways on how to convert a tuple to a set"""


def main():
    """Start the program and run all steps in order."""

    # Method 1: Use of the set() Constructor
    my_tuple1 = (1, 2, 2, 3, 4)
    my_set1 = set(my_tuple1)

    print(my_set1)
    # Output: {1, 2, 3, 4}

    # Method 2: Use of Set Comprehension
    my_tuple2 = (1, 2, 3, 4)

    # Direct conversion
    my_set2 = {item for item in my_tuple2}

    # Alternative: Conversion with a condition (e.g., keeping only even numbers)
    even_set = {item for item in my_tuple2 if item % 2 == 0}

    print(my_set2)
    # Output: {1, 2, 3, 4}

    print(even_set)
    # Output: {2, 4}

    # Method 3: Use of Iterables Unpacking (* Operator)
    my_tuple3 = ("a", "b", "c")
    my_set3 = {*my_tuple3}

    print(my_set3)
    # Output: {'a', 'b', 'c'}

    # Method 4: Use of a for Loop
    my_tuple4 = (10, 20, 30)
    my_set4 = set()

    for item in my_tuple4:
        my_set4.add(item)

    print(my_set4)
    # Output: {10, 20, 30}


if __name__ == "__main__":
    main()
