"""Different ways on how to convert a set to a tuple"""


def main():
    """Start the program and run all steps in order."""

    my_set1 = {1, 2, 3, 4}
    my_set2 = {"apple", "banana", "cherry"}
    my_set3 = {40, 10, 30, 20}
    my_set4 = {"a", "b", "c"}
    my_set5 = {10, 20, 30}

    # Method 1: Use of the tuple() function
    my_tuple1 = tuple(my_set1)

    print(my_tuple1)
    # Output: (1, 2, 3, 4)

    # Method 2: Use of the Unpacking Operator *
    my_tuple2 = (*my_set2,)

    print(my_tuple2)
    # Output: ('banana', 'cherry', 'apple')

    # Method 3: Use of the sorted() Function
    my_tuple3 = tuple(sorted(my_set3))

    print(my_tuple3)
    # Output: (10, 20, 30, 40)

    # Method 4: Using a Generator Expression
    my_tuple4 = tuple(item for item in my_set4)

    print(my_tuple4)
    # Output: ('a', 'c', 'b')

    # Method 5: Use of a List Comprehension
    my_tuple5 = tuple([item for item in my_set5])

    print(my_tuple5)
    # Output: (10, 20, 30)


if __name__ == "__main__":
    main()
