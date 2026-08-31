"""Different ways on how to convert a number to a string"""

import ast
import json
import re


def main():
    """Start the program and run all steps in order."""

    string_data1 = "{'name': 'Alice', 'age': 30, 'city': 'New York'}"
    json_string = '{"brand": "Ford", "model": "Mustang", "year": 1964}'
    string_data2 = "apple:5, banana:3, orange:2"
    string_data3 = "user_id=101 & session_token=A8F92 & status=active"

    # Method 1: Use of ast.literal_eval()

    # Safely parse the string literal
    dict_data = ast.literal_eval(string_data1)

    print(dict_data)
    # {'name': 'Alice', 'age': 30, 'city': 'New York'}

    print(type(dict_data))
    # <class 'dict'>

    # Method 2: Use of json.loads()
    dict_data = json.loads(json_string)

    print(dict_data)
    # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

    print(type(dict_data))
    # <class 'dict'>

    # Method 3: String Splitting & Comprehension (Best for Custom Formats)

    # Split by comma first, then by colon for each pair
    dict_data = {
        item.split(":")[0].strip(): int(item.split(":")[1].strip())
        for item in string_data2.split(",")
    }

    print(dict_data)
    # {'apple': 5, 'banana': 3, 'orange': 2}

    print(type(dict_data))
    # <class 'dict'>

    # Method 4: Regular Expressions (re) (Advanced Custom Formats)

    # Find all word/number combinations separated by an equals sign
    pairs = re.findall(r"(\w+)=(\w+)", string_data3)
    dict_data = dict(pairs)

    print(dict_data)
    # {'user_id': '101', 'session_token': 'A8F92', 'status': 'active'}

    print(type(dict_data))
    # <class 'dict'>


if __name__ == "__main__":
    main()
