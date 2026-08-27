"""Different ways on how to remove all duplicates from a list"""

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

    unique_names1 = list(dict.fromkeys(original_name_list))

    print(f"Unique List 1: \n{unique_names1}\n")
    print(f"No. of items: {len(unique_names1)}\n")

    print("---------------------------------------------------- \n")
    print(
        "Method 2 - Converting list to set, and returning it back to a list (random order)\n"
    )

    unique_names2 = list(set(original_name_list))

    print(f"Unique List 2: \n{unique_names2}\n")
    print(f"No. of items: {len(unique_names2)}\n")

    print("---------------------------------------------------- \n")
    print("Method 3 - Using For Loop \n")

    unique_names3 = []
    for name in original_name_list:
        if name not in unique_names3:
            unique_names3.append(name)

    print(f"Unique List 3: \n{unique_names3}\n")
    print(f"No. of items: {len(unique_names3)}")


if __name__ == "__main__":
    main()
