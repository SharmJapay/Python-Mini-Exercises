"""Different ways on how to convert a tuple to a string"""

from functools import reduce
import operator


def main():
    """Start the program and run all steps in order."""

    # Case 1: Merging Elements into a Single String

    my_tuple1 = ("Learn", "Python", "Programming")
    my_tuple2 = ("Design", 101, True)
    my_tuple3 = ("Code", 2026, "AI")
    my_tuple4 = ("a", "b", "c")
    my_tuple5 = ("A", "B", "C")

    # Method 1: Use of str.join()

    # Joined with a space
    result_space1 = " ".join(my_tuple1)

    print(result_space1)
    # Output: Learn Python Programming

    # Joined with no spaces
    result_flat1 = "".join(my_tuple1)

    print(result_flat1)
    # Output: LearnPythonProgramming

    # Method 2: Use of join() with a Generator Expression
    result1 = " ".join(str(item) for item in my_tuple2)

    print(result1)
    # Output: Design 101 True

    # Method 3: Use of join() and map() function
    result2 = "-".join(map(str, my_tuple3))

    print(result2)
    # Output: Code-2026-AI

    # Method 4: Use of a Standard for Loop
    result3 = ""

    for item in my_tuple4:
        result3 += str(item)

    print(result3)
    # Output: abc

    # Method 5: Use of functools.reduce() and operator.add
    result4 = reduce(operator.add, my_tuple5)

    print(result4)
    # Output: ABC


if __name__ == "__main__":
    main()
