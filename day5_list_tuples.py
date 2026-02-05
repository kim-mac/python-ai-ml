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
"""
def main():
    print(f"{r}")
    arr() 

def arr(r):
    arrays = [1,2,3,4,5]

    for i in range(len(arrays)):
       if arrays[i] == 3:
         return i 

main()
"""
#exercise

expense_data = [2200,2350,2600,2130,2190]

print("i spent",expense_data[2]-expense_data[1], "extra")

