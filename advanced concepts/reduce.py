from functools import reduce
a = [1,2,3,4,5,6]
# [3,3,4,5,6] , [6,4,5,6] , [10,5,6,] , [15,6] [21]

def sum(a,b):
  return a+b

c = reduce(sum, a) #applies the func to all the values one by one ( or two by two , no of values you passed in function arg)
print(c)