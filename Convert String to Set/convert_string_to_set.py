"""Different ways on how to convert a string to a set"""


def main():
    """Start the program and run all steps in order."""

    # Case 1: Convert to a Set of Individual Characters

    text = "Hello World!"

    # Method 1: Use of set() Constructor:
    char_set1 = set(text)

    print(char_set1)
    # Output: {'!', 'r', 'l', 'o', ' ', 'H', 'W', 'd', 'e'}

    # Method 2: Use of Set Comprehension
    char_set2 = {char for char in text}

    print(char_set2)
    # Output: {'!', 'r', 'l', 'o', ' ', 'H', 'W', 'd', 'e'}

    # Case 2: Convert to a Set of Words or Substrings

    text1 = "apple banana apple cherry"

    # Method 1: Using split() with set()
    word_set1 = set(text1.split())

    print(word_set1)
    # Output: {'apple', 'banana', 'cherry'}

    # Method 2: Use of Set Comprehension with split()
    word_set2 = {word.lower() for word in text1.split()}

    print(word_set2)
    # Output: {'apple', 'banana', 'cherry'}

    # Case 3: Store the Entire String as a Single Element

    text2 = "hello"

    # Method 1: Use of Literal Curly Braces {}
    string_set1 = {text2}

    print(string_set1)
    # Output: {'hello'}

    # Method 2: Wrapping in an Iterable inside set()
    string_set2 = set([text2])

    print(string_set2)
    # Output: {'hello'}

    # Method 3: Use of .add() on an Empty Set
    string_set3 = set()
    string_set3.add(text2)

    print(string_set3)
    # Output: {'hello'}


if __name__ == "__main__":
    main()
