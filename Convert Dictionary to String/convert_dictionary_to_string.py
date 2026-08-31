"""Different ways on how to convert a dictionary to a string"""

import json
import pickle


def main():
    """Start the program and run all steps in order."""

    my_dict1 = {"name": "Alice", "age": 30, "city": "New York"}
    my_dict2 = {"Apple": 3, "Banana": 2, "Cherry": 5}
    my_dict3 = {"name": "Alice", "age": 30}

    # Method 1: Use of built-in str() function
    result1 = str(my_dict1)

    print(result1)
    # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

    print(type(result1))
    # Output: <class 'str'>

    # Methods 2: Use of the json.dumps() method
    json_string = json.dumps(my_dict1)

    print(json_string)
    # Output: {"name": "Alice", "age": 30, "city": "New York"}

    # Convert to pretty-printed string
    pretty_json = json.dumps(my_dict1, indent=4)

    print(pretty_json)
    # Output:
    # {
    #     "name": "Alice",
    #     "age": 30,
    #     "city": "New York"
    # }

    # Method 3: Use of List Comprehension with str.join()
    result2 = ", ".join([f"{key}={value}" for key, value in my_dict2.items()])

    print(result2)
    # Output: Apple=3, Banana=2, Cherry=5

    # Method 4: Use of the pickle Module
    byte_string = pickle.dumps(my_dict3)

    print(byte_string)
    # Output: b'\x80\x04\x95\x1e\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x05Alice\x94\x8c\x03age\x94K\x1es.'


if __name__ == "__main__":
    main()
