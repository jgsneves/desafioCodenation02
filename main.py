

class Department:
    def __init__(self, name, code):
        self._name = name
        self._code = code


class Employee:
    def __init__(self, code, name, salary):
        if (type(self) == Employee):
            raise TypeError('Proibido instanciamento direto.')
        else:
            self.code = code
            self.name = name
            self.salary = salary

    def calc_bonus(self):
        pass

    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_department(self):
        return self._departament

    def set_department(self, name, code):
        self._departament = Department(name, code)


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)
        self._sales = 0

    def get_sales(self):
        return self._sales

    def put_sales(self, value):
        self._sales = self._sales + value

    def get_department(self):
        return self._departament

    def set_department(self, name, code):
        self._departament = Department(name, code)

    def calc_bonus(self):
        return self._sales * 0.15
