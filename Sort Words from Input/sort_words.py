"""Different ways on how to sort a words from input (Alphabetical and Reverse Order)"""


def main():
    """Start the program and run all steps in order."""

    user_input = input("Enter words separated by single space: ")

    # Make a list out of user input (except all extra spaces)
    word_list1 = [word for word in user_input.split(" ") if word != ""]
    word_list2 = word_list1.copy()
    word_list3 = word_list1.copy()

    print("\nMethod 1 - Sort using .sort() method of lists (Touches original list) \n")
    print(f"\nOriginal {word_list1 = }\n")

    word_list1.sort()

    print("Sorted List:")

    for word in word_list1:
        print(word)

    print("\n---------------------------------------------------- \n")
    print("Method 2 - Sort using sorted() python function (Renders a new list) \n")
    print(f"\nOriginal {word_list2 = }\n")

    sorted_names = sorted(word_list2)

    print("Sorted List:")

    for word in sorted_names:
        print(word)

    print("\n---------------------------------------------------- \n")
    print("Method 3 - Sort the new list using Bubble sort \n")
    print(f"\nOriginal {word_list3 = }\n")

    len_word_list = len(word_list3)
    for i in range(len_word_list):
        for j in range(0, len_word_list - i - 1):
            if word_list3[j] > word_list3[j + 1]:
                # Swap values of two index
                word_list3[j], word_list3[j + 1] = word_list3[j + 1], word_list3[j]

    print("Sorted List:")

    for word in word_list3:
        print(word)


if __name__ == "__main__":
    main()
