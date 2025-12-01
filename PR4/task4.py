class Employee:
    def __init__(self, last_name, salary):
        self.__last_name = last_name
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def raise_salary(self, amount):
        if amount < 0:
            raise ValueError("Сумма повышения не может быть отрицательной")
        self.__salary += amount
        return self.__salary
