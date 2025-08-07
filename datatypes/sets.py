set1 = {3,45,6,7}
print(set1,type(set1 ))
#print(s[2]) not allowed
set1.add(52)
print(set1)
set1.add(24)
print(set1)
set1.remove(24)
print(set1)
set1.discard(45)
print(set1)
set1.pop()
print(set1)

#set operations
a = {34,56,7,8}
b = {32,52,42,8}
c = a.union(b) #adds all elements
print(c)
d = a.intersection(b) #common elements
print(d)