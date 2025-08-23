class Employee:
  company = "Asus" #class attribute

  def __init__(self, salary, name, bond, company ):
    self.salary = salary #creates an instance attribut of name salary and assign it with salary
    self.name = name
    self.bond = bond
    self.company = company

  def get_salary(self):
    return self.salary

  def get_info(self):
    print(f"the name of the employee is {self.name}. salary is {self.salary} and the bond period is {self.bond} years")

e1 = Employee(32000, "john", 4,'tesla' )
print(e1.company) #will always print instance attribute whenever present 
print(Employee.company)

#object introspection 
#print(dir(e1))