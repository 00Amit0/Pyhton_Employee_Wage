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
            if check == 0:
                print('{0} : Employee is Absent'.format(check))
            else:
                print('{0} : Employee is Present'.format(check)
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    try:
        emp = EmployeeWage()
        emp.attendance()
    except Exception as e:
        logging.warning("Warning ..")
        print(e)
