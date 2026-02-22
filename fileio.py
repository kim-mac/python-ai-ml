#saving in a list
"""
name = []

for i in range(3):
    name.append(input("Enter a name: "))
    

for i in sorted(name):
     print(i)  
"""
""" 
#saving in a file       

name = input("Enter you name: ")

file = open("names.txt", "a") 
file.write(f"{name}\n")
file.close

#saving a file alternate way(no need to close)

name = input("Enetr your name")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
     """

#read from files

""" with open("names.txt", "r") as file:
    lines = file.readline() #readline reads just one line

for line in lines:
    print(line.rstrip(), end="")  
 """

#read from files compact way
""" with open("names.txt", "r") as file:
    for line in file:
        print(line.rstrip())    
 """
#reading and sorting

""" names=[]

with open("names.txt", "r") as file:
    for lines in file:

        names.append(lines.rstrip())

for i in sorted(names, reverse=True):
    print(f"{i}")    
 """
#using csv
with open("names.csv", "r") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is {row[1]}")    