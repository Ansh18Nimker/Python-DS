a = (2,3,4,5)
print(a)
print(a[2])
B = (5, ) # tuple with one element , comma is must to make a single element tuple
print(B)
#tuple unpacking
tu = (1,2,3,4,5)
a,b,c,d,e = tu
print(a,c,e)
#tuple methods
tup = (23,25,64,745,64)
print(tup.count(64))
print(tup.index(23))
#tuples are faster than lists
#used as dictionary keys
#safe from unintended modifications (since they are immutable)