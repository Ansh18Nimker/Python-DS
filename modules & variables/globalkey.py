def sum(a,b):
  print("summing ")
  c = a+b
  global z #now a global varibale, wont be deleted or overriden
  z = 0
  return c


z = 3
print(sum(3,12))
print(z)
 