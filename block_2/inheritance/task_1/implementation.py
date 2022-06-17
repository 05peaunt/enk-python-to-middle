class Employee:
    """Сотрудник."""
    def __init__(self, salary):
        self.salary = salary

class CEO(Employee):
    def __init__(self, salary):
        super().__init__(salary)
        self.dev = 1
        self.analyse = 1
        self.test = 1

class Developer(Employee):
    def __init__(self, salary):
        super().__init__(salary)
        self.dev = 1
        self.analyse = 0
        self.test = 0

class Analyst(Employee):
    def __init__(self, salary):
        super().__init__(salary)
        self.dev = 0
        self.analyse = 1
        self.test = 0

class Tester(Employee):
    def __init__(self, salary):
        super().__init__(salary)
        self.dev = 0
        self.analyse = 0
        self.test = 1

class TeamLead(Employee):
    def __init__(self, salary):
        super().__init__(salary)
        self.dev = 1
        self.analyse = 0
        self.test = 1

class ProductOwner(Employee):
    def __init__(self, salary):
        super().__init__(salary)
        self.dev = 0
        self.analyse = 1
        self.test = 1

class Freelancer():
    def __init__(self, position):
        self.dev = position.dev
        self.analyse = position.analyse
        self.test = position.test


class Organization:
    """Организация."""

    analyse = 0
    dev = 0
    test = 0
    total_salary = 0

    @property
    def can_analyze_count(self):
        """Количество сотрудников, которые могут анализировать задачи."""
        return self.analyse

    @property
    def can_develop_count(self):
        """Количество сотрудников, которые могут разрабатывать задачи."""
        return self.dev

    @property
    def can_test_count(self):
        """Количество сотрудников, которые могут тестировать задачи."""
        return self.test

    def accept_employee(self, employee):
        """Принимает сотрудника на работу."""
        if not isinstance(employee, Employee):
            raise TypeError
        if isinstance(employee, CEO):
            self.analyse += 1
            self.dev += 1
            self.test += 1
            self.total_salary += employee.salary
        elif isinstance(employee, Developer):
            self.dev += 1
            self.total_salary += employee.salary
        elif isinstance(employee, Tester):
            self.test += 1
            self.total_salary += employee.salary
        elif isinstance(employee, Analyst):
            self.analyse += 1
            self.total_salary += employee.salary
        elif isinstance(employee, TeamLead):
            self.dev += 1
            self.test += 1
            self.total_salary += employee.salary
        elif isinstance(employee, ProductOwner):
            self.analyse += 1
            self.test += 1
            self.total_salary += employee.salary

    def accept_employees(self, *args):
        """Принимает сотрудников на работу."""
        for employee in args:
            if isinstance(employee, CEO):
                self.analyse += 1
                self.dev += 1
                self.test += 1
                self.total_salary += employee.salary
            elif isinstance(employee, Developer):
                self.dev += 1
                self.total_salary += employee.salary
            elif isinstance(employee, Tester):
                self.test += 1
                self.total_salary += employee.salary
            elif isinstance(employee, Analyst):
                self.analyse += 1
                self.total_salary += employee.salary
            elif isinstance(employee, TeamLead):
                self.dev += 1
                self.test += 1
                self.total_salary += employee.salary
            elif isinstance(employee, ProductOwner):
                self.analyse += 1
                self.test += 1
                self.total_salary += employee.salary
            elif isinstance(employee, ProductOwner):
                self.analyse += 1
                self.test += 1
                self.total_salary += employee.salary
            elif isinstance(employee, Freelancer):
                self.analyse += employee.analyse
                self.test += employee.test
                self.dev += employee.dev

    def calculate_salary(self):
        """Начисляет заработную плату сотрудникам.

        Returns:
            Возвращает общую сумму всех начислений
        """
        return self.total_salary




