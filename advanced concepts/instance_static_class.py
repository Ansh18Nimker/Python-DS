class Employee:
  company = "HP"
  def __init__(self, name , salary):
    self.name = name 
    self.salary = salary
  
  # instance method (Default method)
  
  def print_info(self):
    info = f"the name is {self.name} and the salary is {self.salary}"
    print(info)
  
  @staticmethod #static method, doesn't needs self 
  def sum(a,b):
    return a+b

  @classmethod #class methods
  def print_company(cls):
    print(cls.company)

  @classmethod #class methods
  def change_company(cls, new_company):
    cls.company = new_company

e1 = Employee("jack", 3455)
e2 = Employee("john", 34555)
# print(Employee.company)
# print(Employee.name) #will throw an error
# e1.print_info()
# e2.print_info()
# print(e2.sum(5,23)) 
print(Employee.company)
e1.change_company("Acer")
print(Employee.company)
