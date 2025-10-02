def is_greater_than_9(x):
  if x>9:
    return True
  else:
    return False

a = [1,2,4, 5,31,21,32,4335,435,132]

new = list(filter(lambda x: x>9, a)) #use list otherwise object value will be returned
print(new)