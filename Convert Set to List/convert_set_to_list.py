"""Different ways on how to convert a set to a list"""


def main():
    """Start the program and run all steps in order."""

    my_set1 = {1, 2, 3, 4, 5}
    my_set2 = {"apple", "banana", "cherry"}
    my_set3 = {5, 1, 3, 8, 4, 2, 6, 9, 10, 7}

    # Method 1: Use of the list() function
    my_list1 = list(my_set1)

    print(my_list1)
    # Output: [1, 2, 3, 4, 5]

    # Method 2: Use of [*set] (Star Unpacking)
    my_list2 = [*my_set2]

    print(my_list2)
    # Output: ['banana', 'apple', 'cherry']

    # Method 3: Using List Comprehension
    my_list3 = [item for item in my_set1]
    squared_list = [item**2 for item in my_set1]

    print(my_list3)
    # Output: [1, 2, 3, 4, 5]

    print(squared_list)
    # Output: [1, 4, 9, 16, 25]

    # Method 4: Use of the sorted() function
    my_list4 = sorted(my_set3)

    print(my_list4)
    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Method 5: Use of For Loop (Manual Iteration)
    my_list5 = []

    for item in my_set3:
        my_list5.append(item)

    print(my_list5)
    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


if __name__ == "__main__":
    main()
