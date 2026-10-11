
def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_rate):
    return gross_salary * tax_rate / 100


def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax

def display_salary(name, basic_salary, allowance,
                   gross_salary, tax, net_salary):
    print("\n===== EMPLOYEE SALARY DETAILS =====")
    print("Employee Name:", name)
    print("Basic Salary:", basic_salary)
    print("Allowance:", allowance)
    print("Gross Salary:", gross_salary)
    print("Tax Amount:", tax)
    print("Net Salary:", net_salary)
    print("===================================")


def main():
    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowance: "))
    tax_rate = float(input("Enter tax rate (%): "))

    gross_salary = calculate_gross_salary(
        basic_salary, allowance
    )

    tax = calculate_tax(gross_salary, tax_rate)

    net_salary = calculate_net_salary(
        gross_salary, tax
    )

    display_salary(name, basic_salary, allowance,
                   gross_salary, tax, net_salary)


if __name__ == "__main__":
    main()
