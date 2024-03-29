class Salary:
    def calculate(self, hours: float) -> float:
        return self.rate * hours


class Promotable:
    def promote(self, _raise: float) -> None:  # _raise so it doesn't clash with Python's raise keyword!
        self.rate += _raise


class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate
 
    def weekly_salary(self) -> float:
        return self.calculate(40)


emp = Employee(14.00)
salary1 = emp.weekly_salary()
print(salary1)

emp.promote(6.00)
salary2 = emp.weekly_salary()
print(salary2)