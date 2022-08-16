import logging
import random

logging.basicConfig(filename='Emp_Wage.log', filemode='w', level=logging.DEBUG)

print("\n")
print("----------Welcome to Employee Wage program----------")
print("\n")


class EmployeeWage:
    def attendance(self):
        logging.debug("Employee wage running")
        try:
            check = random.randint(0, 1)
            wage_per_hour = 20
            emp_wage = 0
            if check == 0:
                print('{0} : Employee is Absent'.format(check))
                emp_wage = wage_per_hour * 0
                print('{0} : is employee\'s wage'.format(emp_wage))
            else:
                print('{0} : Employee is Present'.format(check))
                emp_wage = wage_per_hour * 1
                print('{0} : is employee\'s wage'.format(emp_wage))
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    try:
        emp = EmployeeWage()
        emp.attendance()
    except Exception as e:
        logging.warning("Warning ..")
        print(e)