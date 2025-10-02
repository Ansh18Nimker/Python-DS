# while True:
#     try:
#         a = int(input("enter number 1 = "))
#         b = int(input("enter number 2 = "))
        
#         print(f"the division is {a / b}")

#     except ValueError:
#         print("please dont perform bad typecasts")
    
#     except ZeroDivisionError:
#         print("hey dont divide by zero")

#     except Exception as e:
#         print("some error occured!", e)

a = int(input("enter the number 1 :"))
b = int(input("enter the number 2"))

if b ==0:
  raise ValueError("please dont divide by 0")


print(f"the division is {a/b}")
