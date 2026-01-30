"""
symbol = input("Input your symbol: ")

for i in range(1, 6):
    for j in range(i):
        print(symbol, end="")
    print()
"""

marks = [1,2,3]

for i in range(5):
    score = int(input(f"Enter marks for student {i+1}: "))
    marks.append(score)

print("Marks:", marks)
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))



