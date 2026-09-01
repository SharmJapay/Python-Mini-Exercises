"""Different ways on how to convert a tuple to a list"""


def main():
    """Start the program and run all steps in order."""

    # Method 1: Use of the list() function
    my_tuple1 = (10, 20, 30, 40)
    my_list1 = list(my_tuple1)

    print(my_list1)
    # Output: [10, 20, 30, 40]

    # Method 2: Use of the Unpacking Operator (*)
    my_tuple2 = ("apple", "banana", "cherry")

    # Convert using unpacking
    my_list2 = [*my_tuple2]

    print(my_list2)
    # Output: ['apple', 'banana', 'cherry']

    # Method 3: Use of List Comprehension
    my_tuple3 = (1, 2, 3, 4)
    my_list3 = [item for item in my_tuple3]

    print(my_list3)
    # Output: [1, 2, 3, 4]

    # Method 4: Use of a For Loop
    my_tuple4 = (100, 200, 300)
    my_list4 = []

    # Convert manually
    for item in my_tuple4:
        my_list4.append(item)

    print(my_list4)
    # Output: [100, 200, 300]

    # Method 5: Use of the map() Function
    my_tuple5 = (5, 10, 15)

    # Convert using map() and an identity lambda function
    my_list5 = list(map(lambda x: x, my_tuple5))

    print(my_list5)
    # Output: [5, 10, 15]


if __name__ == "__main__":
    main()
