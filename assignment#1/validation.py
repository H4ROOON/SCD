"""Mark validation rules, independent of user input and display code."""


class InvalidMarkError(ValueError):
    """Raised when a numeric mark falls outside the allowed interval."""


def validate_mark(mark):
    """Raise InvalidMarkError for a mark outside 0 through 100.

    The condition intentionally matches the original lab program.
    The original does not handle non-numeric input in this function.
    """
    if mark < 0 or mark > 100:
        raise InvalidMarkError("Invalid marks. Enter 0-100.")
