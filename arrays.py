#exercise

expense_data = [2200,2350,2600,2130,2190]

print("i spent",expense_data[2]-expense_data[1], "extra")

print("Total expense in first three months is", expense_data[0]+expense_data[1]+expense_data[2])

print("Did i spent 2000 in any months", 2000 in expense_data)

expense_data.append(1980)
print("spending for the month of june", expense_data)

expense_data[3] -= 200
print("New data", expense_data)

#exercise 2
heros=['spider man','thor','hulk','iron man','captain america']

print("The length of th list is", len(heros))

heros.append("black panther")
print("new list is", heros)

heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)

heros[1:3] = ["Doctor strange"]
print(heros)

heros.sort()
print(heros)


user_input = int(input("Enter your number"))

for i in range(user_input):
    if i % 2 != 0:
        print(i)