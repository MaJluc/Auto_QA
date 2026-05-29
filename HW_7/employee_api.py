import requests

class EmployeeApi:

    def __init__(self, url):
        self.url = url

    def create_employ(self, data_json, user=None, password=None):
        url = self.url + '/employee/create'
        if user and password:
            token = self.get_token(user, password)
            url = f"{self.url}/employee/create?client_token={token}"
        resp = requests.post(url, json=data_json)

        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_employee_by_id(self, id):
        resp = requests.get(self.url + f'/employee/info/{id}')
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()


    def get_token(self, user, password):
        creds = {"username": user, "password": password}
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["user_token"]

    def edit_employee(self, employee_id, last_name, user, password):
        client_token = self.get_token(user, password)
        url_with_token = f"{self.url}/employee/change/{employee_id}?client_token={client_token}"

        employee_data = {
            "last_name": last_name
        }
        resp = requests.patch(url_with_token, json=employee_data)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_companies(self):
        resp = requests.get(self.url + '/company/list')

        return resp.json() if resp.status_code == 200 else None

    # def get_employees(self):
    #     # Пробуем разные возможные endpoint'ы
    #     endpoints = ['/employee/list', '/employee', '/employees']
    #     for endpoint in endpoints:
    #         resp = requests.get(self.url + endpoint)
    #         if resp.status_code == 200:
    #             print(f"Найден рабочий endpoint: {endpoint}")
    #             return resp.json()
    #     print("Не найден рабочий endpoint для списка сотрудников")
    #     return None

    def find_employee_by_email(self, email):
        # Перебираем ID с 1, пока не найдём нужный email
        employee_id = 1
        max_attempts = 100  # Защита от бесконечного цикла

        while employee_id <= max_attempts:
            try:
                employee = self.get_employee_by_id(employee_id)
                if employee.get("email") == email:
                    print(f"Найден сотрудник с ID {employee_id}")
                    employee["id"] = employee_id

                    return employee
            except:
                # Если сотрудник не существует, продолжаем поиск
                pass
            employee_id += 1

        print(f"Сотрудник с email {email} не найден в первых {max_attempts} ID")
        return None

    def create_company(self, company_data, user=None, password=None):
        url = self.url + '/company/create'
        if user and password:
            token = self.get_token(user, password)
            url = f"{self.url}/company/create?client_token={token}"
        resp = requests.post(url, json=company_data)

        return resp.json() if resp.status_code in [200, 201] else None
