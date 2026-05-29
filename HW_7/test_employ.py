from employee_api import EmployeeApi
import pytest


base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)

@pytest.fixture(scope="module")  # Fixture для создания сотрудника и возврата его email
def employee_email():
    company_data = {
        "name": "Maxxwell",
        "description": "Company for employee creation"
    }
    company = api.create_company(company_data, user="harrypotter", password="expelliarmus")

    if company and "id" in company:
        company_id = company["id"]
    else:
        raise Exception("Failed to create company")

    employee_json = {
            "first_name": "Maxx",
            "last_name": "string",
            "middle_name": "string",
            "company_id": company_id,
            "email": "maxx@example.com",
            "phone": "string",
            "birthdate": "1979-01-01",
            "is_active": True
    }
    new_employee = api.create_employ(data_json=employee_json, user="harrypotter", password="expelliarmus")

    assert new_employee["first_name"] == "Maxx"
    # print(f"Создан сотрудник с ID: {new_employee.get('id')}")
    print(f"Email сотрудника: {employee_json['email']}")

    return employee_json['email']

def test_create_employee(employee_email):
    assert employee_email == "maxx@example.com"

def test_get_employee(employee_email):
    employee = api.find_employee_by_email(employee_email)
    if not employee:
        raise Exception(f"Сотрудник с email {employee_email} не найден")

    employee_id = employee["id"]
    print(f"Найден сотрудник с ID: {employee_id}")

    employee_info = api.get_employee_by_id(employee_id)

    assert employee_info["first_name"] == "Maxx"


def test_edit_employee(employee_email):
    employee = api.find_employee_by_email(employee_email)
    if not employee:
        raise Exception(f"Сотрудник с email {employee_email} не найден")

    employee_id = employee["id"]
    print(f"Найден сотрудник с ID: {employee_id}")

    mod_employee = api.edit_employee(employee_id, "Bugger", "harrypotter","expelliarmus")

    assert mod_employee["last_name"] == "Bugger"
