import csv
import json


def read_csv() -> list:
    employee = []
    with open('database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = dict()
            temp["employee_id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee


def find_employee(employees, emp_id):
    for employee in employees:
        if employee["employee_id"] == emp_id:
            return employee


def select_staff_by_position(employees, position):
    return list(filter(lambda d: d["position"] == position, employees))


def select_staff_by_salary(employees, min_salary, max_salary):
    return list(filter(lambda d: min_salary <= d["salary"] <= max_salary, employees))


def write_csv(employees: list):
    with open('database.csv', 'w', encoding='utf-8') as f_out:
        csv_writer = csv.writer(f_out)
        for employee in employees:
            csv_writer.writerow(employee.values())


def write_json(employees: list):
    with open('export.json', 'w', encoding='utf-8') as f_out:
        # json.dump(employees, f_out)
        f_out.write(json.dumps(employees))


def add_employee(employees, employee):
    employees.append(employee)


def delete_employee(employees, employee):
    employees.remove(employee)
