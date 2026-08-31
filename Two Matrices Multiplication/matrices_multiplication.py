"""Show how to multiply two matrices based on given number of matrix lines"""

import random


def main():
    """Start the program and run all steps in order."""

    matrix_one, matrix_two, result_matrix = [], [], []

    while True:
        try:
            # Input the desired number of lines in matrices
            matrix_lines = int(
                input(
                    "\nEnter number of matrix lines (e.g. 3 for 3x3 matrix) \nChoose from 2 to 5 only: "
                )
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
            list1.append(random.randint(-10, 10))
            list2.append(random.randint(-10, 10))
            result.append(0)

        matrix_one.append(list1)
        matrix_two.append(list2)
        result_matrix.append(result)

    # Multiply the two matrices
    for index in range(matrix_lines):
        for row in range(matrix_lines):
            result = 0

            for column in range(matrix_lines):
                result += matrix_one[index][column] * matrix_two[column][row]

            result_matrix[index][row] = result

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
