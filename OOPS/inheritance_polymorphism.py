class Animal:
  location = "Australia"
  def __init__(self,name):
    self.name = name
  def speak(self):
    print("speaking now....")

class dog(Animal): #this is how inheritance works in python
  def speak(self):
    super().speak() #we are using speak func of parent class
    print("Woof!")


# = Animal("dog")
#.speak()
d = dog("Bruno")
d.speak()
#print(d.location)

