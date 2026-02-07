"""
symbol = input("Input your symbol: ")

for i in range(1, 6):
    for j in range(i):
        print(symbol, end="")
    print()
"""
"""
marks = []

for i in range(5):
    score = int(input(f"Enter marks for student {i+1}: "))
    marks.append(score)

print("Marks:", marks)
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
"""


def main():    
    array = arr()
    printa(array) 


def arr():
    arrays = [1,2,3,4,5]

    for i in range(len(arrays)):
       if i == 3:
         return i
       
    
    return("Not found") 
       
def printa(n):
   print(n)
           

main()



