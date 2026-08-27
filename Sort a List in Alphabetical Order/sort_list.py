"""Different ways on how to sort a list in alphabetical order"""

import json
import random

FILENAME = "fruits.json"


def get_fruits() -> list:
    """Returns a random list of fruits from file"""

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            fruits = json.load(file)
        random.shuffle(fruits)
        return fruits

    except Exception:
        print("An error occured while opening the file")


def main() -> None:
    """Start the program and run all steps in order."""

    original_list = get_fruits()
    fruits1 = original_list
    fruits2 = original_list
    fruits3 = original_list

    print(f"\nOriginal Fruits List: \n{original_list}\n")
    print(f"No. of items: {len(original_list)} \n")

    print("---------------------------------------------------- \n")
    print("Method 1 - Sort using .sort() method of lists (Touches original list) \n")

    fruits1.sort()

    print(f"Sorted Fruits 1: \n{fruits1}\n")
    print(f"No. of items: {len(fruits1)}\n")

    print("---------------------------------------------------- \n")
    print("Method 2 - Sort using sorted() python function - renders new list \n")

    fruits2 = sorted(fruits2)

    print(f"Sorted Fruits 2: \n{fruits2}\n")
    print(f"No. of items: {len(fruits2)}\n")

    print("---------------------------------------------------- \n")
    print("Method 3 - Sort the new list using Bubble sort \n")

    len_names = len(fruits3)
    for i in range(len_names):
        for j in range(0, len_names - i - 1):
            if fruits3[j] > fruits3[j + 1]:
                # Swap the names
                fruits3[j], fruits3[j + 1] = (
                    fruits3[j + 1],
                    fruits3[j],
                )

    print(f"Sorted List 3: \n{fruits3}\n")
    print(f"No. of items: {len(fruits3)}")


if __name__ == "__main__":
    main()
