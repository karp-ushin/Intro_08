from view import *
from model import *
employees = list()


def run_work():
    global employees
    employees = read_csv()
    # employee = {}
    while True:
        choice = show_menu()
        if choice == 1:         # find employee
            employee_id = get_employee_id()
            employee = find_employee(employees, employee_id)
            display_employee(employee)
        elif choice == 2:         # selection of employees by position
            position = get_employee_position()
            staff = select_staff_by_position(employees, position)
            display_staff(staff)
        elif choice == 3:        # selection of employees by salary
            min_salary, max_salary = get_salary_boundaries()
            staff = select_staff_by_salary(employees, min_salary, max_salary)
            display_staff(staff)
        elif choice == 4:        # add employee
            correct_id = False
            employee = dict()
            trial_id = 0
            while not correct_id:
                trial_id = get_employee_id()
                ids = [employee["employee_id"] for employee in employees]
                if trial_id not in ids:
                    correct_id = True
                else:
                    id_is_in_use()
            employee["employee_id"] = trial_id
            employee.update(get_employee_info())
            add_employee(employees, employee)
            report_success()
        elif choice == 5:       # delete employee
            delete()
            report_success()
        elif choice == 6:       # update employee data
            employee_id = delete()
            temp = dict()
            temp["employee_id"] = employee_id
            temp.update(get_employee_info())
            add_employee(employees, temp)
            report_success()
        elif choice == 7:
            write_json(employees)
            report_success()
        elif choice == 8:
            write_csv(employees)
            report_success()
        elif choice == 9:
            break


def delete():
    employee_id = get_employee_id()
    employee = find_employee(employees, employee_id)
    delete_employee(employees, employee)
    return employee_id
