class Employee:  #dunder methods are shortforms for __methods eg __init__ , __str__
  company = "HP"
  def __init__(self , name , salary):
    self.name = name
    self.salary = salary

  def __str__(self):
    return f"the name is {self.name} and salary is {self.salary}"
  
  def __repr__(self): #used by devs to debug
    return f"name: {self.name}\nsalary: {self.salary}"
  
  def __len__(self):
    return len(self.name) #or we can use print(len(e.name))

e = Employee("Ansh", 56000)
print(len(e))
# print(e.name , e.salary)
# print(str(e))
# print(repr(e))



