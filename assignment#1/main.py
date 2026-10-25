"""Entry point: coordinate input, validation, calculations, and output."""

from validation import InvalidMarkError, validate_mark
from calculations import calculate_total, calculate_average, calculate_grade
from display import display_result


def main():
    """Run the student marks application for one student."""
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        while True:
            mark = float(input(f"Enter marks for subject {i + 1}: "))
            try:
                validate_mark(mark)
            except InvalidMarkError as error:
                print(error)
            else:
                marks.append(mark)
                break

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    display_result(name, total, average, grade)


if __name__ == "__main__":
    main()
