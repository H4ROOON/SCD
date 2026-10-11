def get_student_details():
    name = input("Enter student name: ")
    marks = []

    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    return name, marks


def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def determine_result(marks):
    if all(mark >= 40 for mark in marks):
        return "PASS"
    else:
        return "FAIL"


def display_result(name, marks, total, average, grade, result):
    print("\n===== STUDENT RESULT =====")
    print("Student Name:", name)

    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i} Marks: {mark:g}")

    print("Total Marks:", total)
    print(f"Average Marks: {average:.2f}")
    print("Grade:", grade)
    print("Result:", result)
    print("==========================")


def process_student():
    name, marks = get_student_details()

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = determine_grade(average)
    result = determine_result(marks)

    display_result(name, marks, total, average, grade, result)


if __name__ == "__main__":
    process_student()
