"""Remove all duplicates in a list and then sort the list"""

import json
import random

FILENAME = "names.json"


def get_names() -> list:
    """Returns a random list of names from file"""

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            names = json.load(file)
        random.shuffle(names)
        return names

    except Exception:
        print("An error occured while opening the file")


def main() -> None:
    """Start the program and run all steps in order."""

    original_name_list = get_names()
    print(f"\nOriginal Name List: \n{original_name_list}\n")
    print(f"No. of items: {len(original_name_list)} \n")

    print("---------------------------------------------------- \n")
    print(
        "Method 1 - Converting list to dictionary as keys, and returning it back to a list \n"
    )

    # Method 1 - Converting list to dictionary (as keys), and returning it back to a list
    # Sort using .sort() method of lists (Touches original list)
    unique_names1 = list(dict.fromkeys(original_name_list))
    unique_names1.sort()

    print(f"Sorted List 1: \n{unique_names1}\n")
    print(f"No. of items: {len(unique_names1)}\n")

    print("---------------------------------------------------- \n")
    print("Method 2 - Converting list to set, and returning it back to a list \n")

    # Method 2 - Converting list to set, and returning it back to a list
    # Sort using sorted() python function - renders new list
    unique_names2 = list(set(original_name_list))
    unique_names2 = sorted(unique_names2)

    print(f"Sorted List 2: \n{unique_names2}\n")
    print(f"No. of items: {len(unique_names2)}\n")

    print("---------------------------------------------------- \n")
    print("Method 3 - Using of For Loop \n")

    # Method 3 - Using of For Loop
    # Sort the new list using Bubble sort
    unique_names3 = []
    for name in original_name_list:
        if name not in unique_names3:
            unique_names3.append(name)

    len_names = len(unique_names3)
    for i in range(len_names):
        for j in range(0, len_names - i - 1):
            if unique_names3[j] > unique_names3[j + 1]:
                # Swap the names
                unique_names3[j], unique_names3[j + 1] = (
                    unique_names3[j + 1],
                    unique_names3[j],
                )

    print(f"Sorted List 3: \n{unique_names3}\n")
    print(f"No. of items: {len(unique_names3)}")


if __name__ == "__main__":
    main()
