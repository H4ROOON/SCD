# Week 4 Laboratory — Complete Written Answers

## Part A — Code archaeology (original code, only comments added)

The numbered responsibility labels below identify original statements;
**do not refactor the original program during Part A**.

```python
def main():
    name = input("Enter student name: ")      # INPUT
    marks = []                                 # INPUT data collection

    for i in range(3):                         # INPUT: three subjects
        mark = float(input(f"Enter marks for subject {i + 1}: "))  # INPUT

        while mark < 0 or mark > 100:           # VALIDATION
            print("Invalid marks. Enter 0-100.")  # VALIDATION feedback
            mark = float(input(f"Enter marks for subject {i + 1}: "))  # INPUT retry

        marks.append(mark)                     # INPUT data collection

    total = sum(marks)                         # CALCULATION
    average = total / len(marks)               # CALCULATION

    if average >= 80:                          # GRADING / BUSINESS RULE
        grade = "A"
    elif average >= 70:                        # GRADING / BUSINESS RULE
        grade = "B"
    elif average >= 60:                        # GRADING / BUSINESS RULE
        grade = "C"
    elif average >= 50:                        # GRADING / BUSINESS RULE
        grade = "D"
    else:                                      # GRADING / BUSINESS RULE
        grade = "F"

    print("\nStudent Result")                # DISPLAY
    print("----------------")                # DISPLAY
    print("Name:", name)                      # DISPLAY
    print("Total:", total)                    # DISPLAY
    print("Average:", average)                # DISPLAY
    print("Grade:", grade)                    # DISPLAY

main()                                         # Program entry point
```

## Part B — Responsibility map

| Responsibility | What it does | File in refactored solution |
|---|---|---|
| Input | Reads student name and three numeric marks; retries out-of-range marks | `main.py` (small console driver) |
| Validation | Checks that a numeric mark is between 0 and 100; specifies the error | `validation.py` |
| Calculation | Computes sum and arithmetic mean | `calculations.py` |
| Grading/business rule | Maps the average to an A/B/C/D/F grade at given thresholds | `calculations.py` |
| Display | Prints the result labels and values in the original console format | `display.py` |

Input remains in `main.py` because this is a very small console application.
If it grows, input handling can be extracted to a dedicated module.

## Part C — Design answers

**1. Why does each module exist?** `main.py` orchestrates the work;
`validation.py` owns the range rule and its error text;
`calculations.py` owns arithmetic and grading rules; `display.py` owns output
formatting. Grouping closely related arithmetic and grading avoids unnecessary
files while keeping UI logic out of domain logic.

**2. Which functions belong in `calculations.py`?**
`calculate_total(marks)`, `calculate_average(marks)`, and
`calculate_grade(average)`.

**3. Should `display.py` calculate the grade? Why?** No. Displaying values and
assigning grades are different reasons to change. `display.py` receives a
precomputed grade rather than knowing grade thresholds.

**4. What should `main.py` coordinate?** Read a name and three marks; call
validation and repeat entry for invalid marks; call total, average, and grade
functions; then pass the result to display.

**5. Which implementation details should other modules not need to know?**
Other modules should not know input prompt text, retry loops, grade thresholds,
or console formatting unless that is their own responsibility. For example,
`display.py` must not know whether 80 is an A, and `calculations.py` must not
know which `print()` statements are used.

## Part D — Implementation decision

`validate_mark(mark)` raises `InvalidMarkError` on a number outside 0–100.
The message is defined in `validation.py`; `main.py` catches that exception,
prints the message, and asks again. Keeping the `float()` conversion outside
the `try` block intentionally preserves the original treatment of nonnumeric
inputs (the original program raises `ValueError` rather than retrying).
Valid numeric marks, input prompt text, grades, and result output are unchanged.

## Part E — Dependency map and answers

```text
                     main.py
                    /   |    \
                   v    v     v
       validation.py calculations.py display.py

  no imports between validation.py, calculations.py and display.py
```

The editable diagram is `docs/diagrams/module_dependencies.drawio`.

**6.** `main.py` directly depends on `validation.py`, `calculations.py`, and
`display.py`.

**7.** No. `display.py` accepts an already calculated grade as an argument.

**8.** No. `calculations.py` returns numerical or grade values; it never prints.

**9.** A GUI could replace the console presentation layer. Calculation and
validation functions would remain intact, and the entry point would call the
GUI instead of `display_result`. Input handling in `main.py` would also need
adapting for a true GUI, but the business logic would not change.

**10.** Necessary: `main.py -> validation.py`,
`main.py -> calculations.py`, and `main.py -> display.py`. Unnecessary:
`display.py -> calculations.py`, `calculations.py -> display.py`, and
`validation.py -> display.py`.

## Part F — Change request test

**11. Grading changes to A >= 85, B >= 75, C >= 65, D >= 55:**
Only `calculate_grade` in `calculations.py` should change (and its related
tests). The delivered code intentionally retains the **original** thresholds.

**12. Result format changes:** Edit `display.py` only (and relevant output
assertions in tests).

**13. Validation message changes:** Edit the error message in `validation.py`
only (and relevant message assertions in tests). `main.py` prints the
exception's message without hard-coding it.

**14. Later GUI output:** Replace `display.py` with a GUI presentation
implementation and update the coordinating entry point. Keep
`calculations.py` unchanged.

## Part G — Verification

| Check | Values | Expected outcome |
|---|---|---|
| Normal case | 75, 82, 68 | Total 225, average 75, grade B |
| Boundary | Average 50 | Grade D |
| Boundary | Average 60 | Grade C |
| Boundary | Average 70 | Grade B |
| Boundary | Average 80 | Grade A |
| Invalid marks | -5, 105 | Show original error text and re-prompt |
| Second student | 90, 95, 85 | Total 270, average 90, grade A |

Run `python -m unittest discover -s tests -v` from the `student_marks` folder.
`tests/test_student_marks.py` also verifies the complete console output.

## Part 11 — Reflection

**15. Functions vs. modules:** Functions split a program into named operations
within a file; modules organize related functions in distinct Python files,
creating visible dependencies and file-level boundaries around responsibilities.

**16. Strongest cohesion:** `calculations.py` has strong functional cohesion:
its three functions are all about producing student result values. It neither
reads input nor prints output. (The other small modules are also focused.)

**17. Example of coupling:** `main.py` imports and calls
`display_result(name, total, average, grade)`; the call depends on that
function's interface. This direct dependency is necessary orchestration
coupling, unlike forcing `display.py` to import grade thresholds.

**18. Modularity and changes:** Changes stay localized: thresholds live in
`calculations.py`, format in `display.py`, and the validation rule/message in
`validation.py`. The other modules can usually remain unchanged.

**19. Module too broad or too small?** The design is proportionate to the lab.
`calculations.py` combines arithmetic and grading because both are related to
computing results; `display.py` is very small but has a separate reason to
change. For a larger system, grading could move to `grading.py` and input into
`input_handler.py`.

## Part 13 — Semester project connection

See `docs/semester_project_template.md`. Fill it with *your real semester
project* responsibilities and dependency sketch; the student marks design is
not automatically the correct model for a different application.

## Part 14 — Reading connection

The separation demonstrates McConnell's information hiding (internal details
stay within their owning modules), high cohesion (related tasks grouped
in a module), low coupling (limited imports), and change isolation (a format
change does not touch calculations).
