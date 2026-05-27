from employee_api import EmployeeApi


base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)

def test_create_employee():
    # Create a new company to get its ID
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



def test_get_employee():
    employee_info = api.get_employee_by_id(8)

    assert employee_info["first_name"] == "Maxx"


def test_edit_employee():
    mod_employee = api.edit_employee(8, "Bugger", "harrypotter","expelliarmus")

    assert mod_employee["last_name"] == "Bugger"
