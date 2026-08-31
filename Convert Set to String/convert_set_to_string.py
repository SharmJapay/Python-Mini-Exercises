"""Different ways on how to convert a set to a string"""

import json


def main():
    """Start the program and run all steps in order."""

    # Case 1: For a Clean, Combined String (No Braces)

    my_set1 = {1, 2, 3, "apple"}
    my_set2 = {11, 12, 13}
    string_set = {"a", "b", "c"}

    # Method 1: Use of join() and map() functions
    result1 = ", ".join(map(str, my_set1))

    print(result1)
    # Output: "1, 2, 3, apple" (order may vary)

    # Method 2: Use of join() with a List Comprehension
    result2 = "".join(str(x) for x in my_set2)

    print(result2)
    # Output: "111213"

    # Method 3: Use of join() directly (Strings Only)
    result3 = "-".join(string_set)

    print(result3)
    # Output: "a-c-b"

    # Case 2: For a Literal Representation (With Curly Braces)

    # Method 1: Use of str() function
    result4 = str(my_set2)

    print(result4)
    # Output: "{11, 12, 13}"

    # Method 2: Use of f-strings
    result5 = f"{my_set2}"

    print(result5)
    # Output: "{11, 12, 13}"

    # Method 3: Use of repr()
    result6 = repr(my_set2)

    print(result6)
    # Output: "{11, 12, 13}"

    # Case 3: For Serialized Outputs (JSON)

    # Method 1: Use of json.dumps()
    result7 = json.dumps(list(my_set2))

    print(result7)
    # Output: "[1, 2, 3]"


if __name__ == "__main__":
    main()
