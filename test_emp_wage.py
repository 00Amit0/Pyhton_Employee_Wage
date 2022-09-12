from employee_wage import Employee, Company
import pytest


def test_employee_class_attributes():
    emp = Employee("Amit", 50, 20, 8)
    assert emp.name == "Amit"
    assert emp.name != ""


def test_company_class_attributes():
    comp = Company("Onextel")
    assert comp.name == "Onextel"
    assert comp.name != ""


def test_attendance():
    emp = Employee("Amit", 50, 20, 8)
    work_hours = emp.attendance(0)
    assert work_hours == 8, "Employee present for full day"
    work_hours = emp.attendance(1)
    assert work_hours == 4, "Employee present for half day"
    work_hours = emp.attendance(2)
    assert work_hours == 0, "Employee absent"


def test_calculate_wage():
    emp = Employee("Amit", 50, 20, 8)
    total_wage = emp.calculate_wage()
    assert total_wage


def test_emp_dict():
    emp = Employee("Amit", 50, 20, 8)
    initial_dict = emp.emp_dict()
    assert initial_dict.get("Name") == "Amit", "Enter key check value"


def test_add_employee():
    emp = Employee("Amit", 50, 20, 8)
    comp = Company("Onextel")
    assert len(comp.employee_dict) == 0, "No employees in company"
    comp.add_employee(emp)
    assert len(comp.employee_dict) == 1, "1 employee joined"


def test_get_employee():
    emp = Employee("Amit", 50, 20, 8)
    comp = Company("Onextel")
    comp.add_employee(emp)
    actual = comp.get_employee(emp.name)
    assert actual.name == "Amit"


def test_delete_employee():
    emp = Employee("Amit", 50, 20, 8)
    comp = Company("Onextel")
    comp.add_employee(emp)
    assert len(comp.employee_dict) == 1
    comp.delete_employee(emp.name)
    assert len(comp.employee_dict) == 0


