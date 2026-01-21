#String Identifier
"""
string = str(input("Enter a sentence:"))

print("Length", len(string))
print("Upper", string.upper())
print("Lower", string.lower())
print("Split", string.split())
print("Word Count", len(string.split()))
"""

#Extracting info
"""
email= str(input("enter your email: "))

username= email[:email.index("@")]
domain = email[email.index("@")+1:]

print(username)
print(domain)
"""

#Palindrome
"""
userinput = input("Enter your input: ")

clean = userinput.lower().strip()

if clean == clean[::-1]:
    print("Its palindrome")
else:
    print("Its not")  
"""

#password checker

password =  (input("Enter your password: "))

has_digit = False
has_upper = False
has_lower = False

if len(password) < 8:
    print("Invalid password")
else:
    for i in password:
        if i.isdigit():
           has_digit = True
        elif i.isupper():
           has_upper = True
        elif i.islower():
           has_lower = True

    if has_digit and has_upper and has_lower:
        print("Strong password")
    else:
        print("Weak password")           


               
