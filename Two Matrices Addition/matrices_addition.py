"""Show how to add two matrices based on given number of matrix lines"""

import random


def main():
    """Start the program and run all steps in order."""

    matrix_one, matrix_two, result_matrix = [], [], []

    while True:
        try:
            # Input the desired number of lines in matrices
            matrix_lines = int(
                input("Enter number of matrix lines (e.g. 3 for 3x3 matrix): ")
            )

            if 2 <= matrix_lines <= 5:
                break

            else:
                print("Invalid number. Choose from 2 to 5 only!")
                continue

        except ValueError:
            print("Error! Valid integer number is only accepted")

    # Create two matrices
    for _ in range(matrix_lines):
        list1, list2, result = [], [], []

        for _ in range(matrix_lines):
            list1.append(random.randint(0, 100))
            list2.append(random.randint(0, 100))
            result.append(0)

        matrix_one.append(list1)
        matrix_two.append(list2)
        result_matrix.append(result)

    # Add the two matrices
    for row in range(matrix_lines):
        for column in range(matrix_lines):
            result_matrix[row][column] = (
                matrix_one[row][column] + matrix_two[row][column]
            )

    print("Matrix One:")
    for row in range(matrix_lines):
        print(matrix_one[row])

    print("\nMatrix Two : ")
    for row in range(matrix_lines):
        print(matrix_two[row])

    print("\nResult Matrix:")
    for row in range(matrix_lines):
        print(result_matrix[row])


if __name__ == "__main__":
    main()
