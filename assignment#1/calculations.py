"""Student result arithmetic and grading business rules."""


def calculate_total(marks):
    """Return the sum of the supplied marks."""
    return sum(marks)


def calculate_average(marks):
    """Return the arithmetic mean of the supplied marks."""
    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    """Return the original A/B/C/D/F grade for an average."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
