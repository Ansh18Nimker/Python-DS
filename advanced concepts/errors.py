while True:
    try:
        a = int(input("enter number 1 = "))
        b = int(input("enter number 2 = "))
        
        print(f"the sum is {a+b}")
    
    except Exception as e:
        print("some error occured" ,e)

# num = int(input("Enter a number: "))
# while num >= 10:  
#     s = 0
#     for digit in str(num):  
#         s += int(digit)
#     num = s

# print("Single digit result:", num) 



