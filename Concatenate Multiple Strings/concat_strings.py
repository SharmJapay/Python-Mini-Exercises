"""Different ways on how to concatenate multiple strings"""

from io import StringIO


def main():
    """Start the program and run all steps in order."""

    greet = greet1 = "\nWelcome to this Python tutorial"
    firstname = input("Enter you first name: ")
    lastname = input("Enter you last name: ")

    # Method 1: Use of + and +=
    name = firstname + " " + lastname
    greet += " " + name
    print(greet)

    # Method 2: Use of f-Strings (Formatted String Literals)
    output = f"{greet1} {firstname} {lastname} \n"
    print(output)

    # Method 3: Use of str.format() Method (older version of f-Strings)
    # Using positional placeholders
    print("Hello, {}. Welcome to {}!".format("Bob", "Earth"))
    # Using keyword placeholders
    print("{greeting}, {name}!\n".format(greeting="Hi", name="Sara"))

    # Method 4: Use of .join() method
    words = ["Python", "is", "awesome"]
    sentence = " ".join(words)  # "Python is awesome"
    together = "".join(words)  # "Pythonisawesome"
    print(sentence)
    print(together, "\n")

    # Method 5: Use of String Literal Adjacency
    long_string = (
        "This is a very long string "
        "that spans across multiple lines "
        "automatically.\n"
    )
    print(long_string)

    # Method 6: Use of Stream Building with io.StringI

    buffer = StringIO()
    buffer.write("First line. ")
    buffer.write("Second line.")

    print(buffer.getvalue())  # "First line. Second line."


if __name__ == "__main__":
    main()
