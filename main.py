from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self._name = name
        self._code = code


class Employee(ABC):
    def __init__(self, code, name, salary, departament):
        self.code = code
        self.name = name
        self.salary = salary
        self._departament = departament

    @abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return 8

    def get_departament(self):
        return self._departament._name

    def set_departament(self, name, code):
        self._departament = Department(name, code)


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self._sales = 0

    def get_sales(self):
        return self._sales

    def put_sales(self, value):
        self._sales = self._sales + value

    def calc_bonus(self):
        return self._sales * 0.15
