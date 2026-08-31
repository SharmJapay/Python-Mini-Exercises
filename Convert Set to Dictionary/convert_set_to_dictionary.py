"""Different ways on how to convert a set to a dictionary"""


def main():
    """Start the program and run all steps in order."""

    my_set = {"apple", "banana", "cherry"}
    values = [100, 200, 300]

    # Method 1: Use of dict.fromkeys()
    my_dict1 = dict.fromkeys(my_set, 0)

    print(my_dict1)
    # Output: {'banana': 0, 'cherry': 0, 'apple': 0}

    # Method 2: Use of Dictionary Comprehension
    my_dict2 = {item: len(item) for item in my_set}

    print(my_dict2)
    # Output: {'banana': 6, 'cherry': 6, 'apple': 5}

    # Method 3: Use of zip() and dict() functions
    my_dict3 = dict(zip(my_set, values))

    print(my_dict3)
    # Output: {'banana': 100, 'cherry': 200, 'apple': 300}

    # Method 4: Use of enumerate() inside a Dictionary Comprehension
    my_dict4 = {item: index for index, item in enumerate(my_set, start=1)}

    print(my_dict4)
    # Output: {'banana': 1, 'cherry': 2, 'apple': 3}

    # Method 5: Using a Traditional for Loop
    my_dict5 = {}

    for item in my_set:
        if "a" in item:
            my_dict5[item] = "Contains 'a'"
        else:
            my_dict5[item] = "No 'a'"

    print(my_dict5)
    # Output: {'banana': "Contains 'a'", 'cherry': "No 'a'", 'apple': "Contains 'a'"}


if __name__ == "__main__":
    main()
