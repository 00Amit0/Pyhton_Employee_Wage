def employee_wage(check):
    try:

        wage_per_hour = 20
        match check:
            case 1:
                print('{0} : Employee is full day present'.format(check))
                daily_wage = wage_per_hour * 8
                print('{0} : is employee\'s wage'.format(daily_wage))
            case 2:
                print('{0} : Employee is part time present'.format(check))
                daily_wage = wage_per_hour * 4
                print('{0} : is employee\'s wage'.format(daily_wage))
            case _:
                print('{0} : Employee is Absent'.format(check))
                daily_wage = wage_per_hour * 0
                print('{0} : is employee\'s wage'.format(daily_wage))

    except Exception as e:
        print(e)


class EmployeeWage:
    pass


if __name__ == "__main__":
    employee_wage(5)
