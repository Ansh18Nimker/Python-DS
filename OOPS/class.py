#class- is a blueprint or a template , eg form for an exam that contains name ,age , electives , father's name etc
 
#object : specific instance created from the template that is class , eg - form which contains the data for "john doe" 

class employee:
  company = "HP"

  def get_salary(self): #self is important here because self is a way to reference the object of the class which is being created
    print(self)
    return 34000

e = employee()  #an object of class employee is created here
print(e.get_salary()) #employee e's get salary method is called
e2 = employee()
print(e2.get_salary())
print(e2.company)