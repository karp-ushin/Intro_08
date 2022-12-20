def show_menu() -> int:
    # print("\n" + "=" * 20)
    # print("Выберите необходимое действие")
    # print("1. Найти сотрудника")
    # print("2. Сделать выборку сотрудников по должности")
    # print("3. Сделать выборку сотрудников по зарплате")
    # print("4. Добавить сотрудника")
    # print("5. Удалить сотрудника")
    # print("6. Обновить данные сотрудника")
    # print("7. Экспортировать данные в формате json")
    # print("8. Экспортировать данные в формате csv")
    # print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


def get_employee_id():
    return int(input("Введите id сотрудника: "))


def display_employee(employee):
    print(*employee.values())


def get_employee_position():
    return input("Введите должность: ")


def display_staff(staff):
    for emp in staff:
        print(*emp.values())


def get_salary_boundaries():
    return float(input("Введите нижнюю границу зарплаты: ")),\
        float(input("Введите верхнюю границу зарплаты: "))


def get_employee_info():
    temp = dict()
    temp["last_name"] = input("Введите фамилию: ")
    temp["first_name"] = input("Введите имя: ")
    temp["position"] = input("Введите должность: ")
    temp["phone_number"] = input("Введите номер телефона: ")
    temp["salary"] = float(input("Введите зарплату: "))
    return temp


def id_is_in_use():
    print("Id занят.")


def report_success():
    print("Выполнено.")
