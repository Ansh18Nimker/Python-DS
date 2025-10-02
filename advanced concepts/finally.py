a = int(input("enter the number 1: "))
b = int(input("entet the number 2: "))

def divide(a, b):

  try:
    c = a/b
    print(c)
    return c

  except Exception as e:
    print(e)
    return None

#this will alaways be executed no matter if try completely executes or not
  finally:
    print("this will always be executed")

a = int(input("enter the number 1: "))
b = int(input("entet the number 2: "))
divide(a, b)
