#Multiplication
"""
num = int(input("Enter your number"))

for i in range(1,11):
    print(f"{num} * {i} = {num * i}")
"""

#Sum of numbers
"""
total = 0

for i in range(1,101):
    total += i

print(total)
"""
#while loop
"""
i = 3
while i !=0:
    print("meow")
    i -= 1
"""

#print meow
"""
while True:
    n = int(input("Enter n"))
    if n < 0:
        print("Invalid value")
        continue
    else:
        break
for i in range(n):
    print("meow")
"""

#pattern
"""
pattern = input("Input your symbol: ")

for i in range(1,6):
    print(f"{pattern * i}")
"""
#pattern reverse
"""
pattern = input("Input your symbol: ")

for i in range(5,0,-1):
    print(f"{pattern * i}")
"""
#pattern new
"""
pattern = "*"

for i in range(1,6):
    print(f"{pattern * i}")

"""

#guess

secrect = 7
guess = 0

while guess != secrect:
    guess = int(input("Enter your number"))

print("Correct")    