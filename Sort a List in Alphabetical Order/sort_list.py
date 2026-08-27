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

    fruits1 = get_fruits()
    fruits2 = fruits1.copy()
    fruits3 = fruits1.copy()

    print("\nMethod 1 - Sort using .sort() method of lists (Touches original list) \n")

    print(f"{fruits1 = } \n")

    fruits1.sort()

    print(f"Sorted fruits1: \n{fruits1}\n")

    print("---------------------------------------------------- \n")
    print("Method 2 - Sort using sorted() python function (Renders a new list) \n")

    print(f"{fruits2 = } \n")

    fruits2 = sorted(fruits2)

    print(f"Sorted fruits2: \n{fruits2}\n")

    print("---------------------------------------------------- \n")
    print("Method 3 - Sort the new list using Bubble sort \n")

    print(f"{fruits3 = } \n")

    len_names = len(fruits3)
    for i in range(len_names):
        for j in range(0, len_names - i - 1):
            if fruits3[j] > fruits3[j + 1]:
                # Swap the names
                fruits3[j], fruits3[j + 1] = (
                    fruits3[j + 1],
                    fruits3[j],
                )

    print(f"Sorted fruits3: \n{fruits3}\n")


if __name__ == "__main__":
    main()
