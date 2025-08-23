class Employee:
  def __init__(self, salary, name, bond):
    self.salary = salary #creates an instance attribut of name salary and assign it with salary
    self.name = name
    self.bond = bond

  def get_salary(self):
    return self.salary

  def get_info(self):
    print(f"the name of the employee is {self.name}. salary is {self.salary} and the bond period is {self.bond} years")

e1 = Employee(25000, "ansh", 4)
print(e1.get_salary())
e1.get_info()
