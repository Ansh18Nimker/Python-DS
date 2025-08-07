#dictionaries
marks = {"ansh":89, "khushal":99, "arti":98}
print(marks,type(marks))
print(marks["arti"])
marks["ansh"] = 92
print(marks)

#dict methods
print(marks.keys()) #prints keys
print(marks.values()) #prints values
print(marks)

#dictionary comprehentsions
tableof5 = {i: 5*i for i in range(1,11)}
print(tableof5)

#subha milte hai ab :)