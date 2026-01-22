#Age Category
"""
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")    
"""
#Grade calculator
"""
grade = int(input("Enter your grade 0-100: "))

if grade > 100:
    print("Invalid grade please enter again")
elif grade >= 90:
    print("grade A")  
elif grade >= 80:
    print("grade B")
elif grade >= 70:
    print ("grade C")
else:
    print("Fail")
"""

#Login authentication
"""
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "admin":
    print("Valid")
else:
    print("Invalid")
"""

#Interger identifier

integer = int(input("Enter you number: "))

if integer < 0:
    print(f"The integer is {integer} and its negative")
elif integer == 0:
    print(f"The integer is {integer}")
elif integer >0:
    print(f"The integer is {integer} and its positive")

if integer % 2 == 0:
    print(f"The integer is {integer} and its even")
else:
    print(f"The integer is {integer} and its odd")

if integer % 3 == 0:
    print(f"The integer {integer} is divisible by 3")
else:
     print(f"The integer {integer} is not divisible by 3")                 