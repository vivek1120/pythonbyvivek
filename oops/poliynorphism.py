class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __lt__(self, other):
        return self.salary < other.salary

employees = [
    Employee("John", 50000),
    Employee("Jane", 60000),
    Employee("Bob", 55000)
]

sorted_employees = sorted(employees)
print(sorted_employees)