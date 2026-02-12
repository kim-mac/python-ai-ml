#SyntaxError - improper syntax or syntax is incomplete
#ValueError - Value entered isnt proper
#NameError - Something is dont defined
"""
#basic
try:
    x = int(input("Enter your number: "))
    print(f"Your number is {x}")
except ValueError:
    print("Your number is not an integer") 


#Format change
try:
    y = int(input("Enter your number: "))
except:
    print("Incorrect input")
else:
    print(f"Your number is {x}")               

#Loop format
while True:
    try:
        x = int(input("Enter your number: "))
    except:
        print("Its not an integer")
    else:
        break

print(f"The number is {x}")


#Function format

def main():

    value = get_int()
    print(f"The value is {value}")

def get_int():

    while True:
        try:
           x = int(input("Enter your number: "))    #(return can be used here as well as "return int(input("Enter your number: "))")
           #return x                (return can be used here as well to make the code shorter)  
        except:
            print("Not an integer")
        else:
            break #/return x     (return can be user here instead of break ad return can break out of the loop as well as return a value, again to make code shorter)

    return x

main()   


#Pass format

def main():
    x = get_int()
    print(f"The number is {x}")

def get_int():
    while True:
        try:
            return int(input("Enter your number: "))
        except:
            pass    #doesnt give any error, passes and lets continue the loop(makes the code shorter)

main()
"""

#prompt format

def main():
    x = get_int("Whats x: ")
    print(f"The number is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass    #doesnt give any error, passes and lets continue the loop(makes the code shorter)

main()