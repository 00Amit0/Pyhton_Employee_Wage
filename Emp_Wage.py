import logging
import random

logging.basicConfig(filename='Emp_Wage.log', filemode='w', level=logging.DEBUG)

print("\n")
print("----------Welcome to Employee Wage program----------")
print("\n")


class EmployeeWage:

    def __init__(self, wage_per_hour, monthly_working_day):
        self.wage_per_hour = wage_per_hour
        self.monthly_working_day = monthly_working_day

    def attendance(self, check):
        """
        Function checks employee present or not
        :return:
        """
        logging.debug("Employee wage running")
        try:
            # check = random.randint(0, 2)
            wage_per_hour = 20
            if check == 0:
                daily_work_hour = 0
                print('{0} : Employee is Absent'.format(check))
                # daily_wage = wage_per_hour * 0
                # print('{0} : is employee\'s wage'.format(daily_wage))
            elif check == 1:
                daily_work_hour = 8
                print('{0} : Employee is Present , Full-Timer '.format(check))
                # daily_wage = wage_per_hour * 8
                # print('{0} : is employee\'s wage'.format(daily_wage))
            else:
                daily_work_hour = 4
                print('{0} : Employee is Present , Part-Timer '.format(check))
        except Exception as ex:
            print(ex)

    def calculating_wage(self):
        """
        Function calculates wage of employee according to his attendance
        :return: nothing
        """
        logging.debug("Program running fine.....")
        try:
            total_wage = 0
            no_of_working_days = 0
            while no_of_working_days < self.monthly_working_day:
                no_of_working_days += 1
                check = random.randint(0, 2)
                daily_work_hour = self.attendance(check)
                daily_wage = self.wage_per_hour * daily_work_hour
                print(f" The daily wage is : {daily_wage}")
                total_wage += daily_wage
            print(f"The monthly wage is : {total_wage}")

        except Exception as e:
            print(e)
            logging.exception("Error occurred , recheck the code")


if __name__ == "__main__":
    try:
        emp = EmployeeWage(20, 20)
        emp.calculating_wage()
    except Exception as e:
        logging.warning("Warning ..")
        print(e)
