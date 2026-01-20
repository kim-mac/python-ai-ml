"""
name = input("Whats your name: ")
#age = int(input("Enter your age: "))

name = name.title().strip()

print("Hello", name, end='\n')
print(f"Hello {name}")
#print( "You are", age, "years old")
"""

#Calculator
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = 5
b = 5

add = a+b
print(f"{add:,}")  #to add comas to numbers

subtract = a-b
print(subtract)

multiplication = a*b
print(multiplication)

division = a/b
print(division)

d2 = a%b
print(d2)
"""

#Temperature converter
"""
temp = float(input("Enetr your temperature in degree celsius: "))
farenheit = (temp * 9/5) + 32

print("Temperature in farenheit is", farenheit)
"""

#Functions
"""
def new(post):            #name = post(value from name is transfered into post & it doesnt have to be same)
    print("Hey", post)

name = input("Whats your name")
new(name)    

def main():
    x = int(input("Enter value for x"))
    print("x cube is", cube(x))

def cube(c):
    return c**3  

main()  
"""

#if-else conditions
grade = int(input("Enter grade of students: "))
if grade >= 100:
    print("Invalid Grade")
    if grade >= 90 and grade<=100:
     print("Grade A")
    elif grade >=80 and grade<90:
     print("Grade B")
    elif grade >= 70 and grade<80:
     print("Grade C")
    


        
