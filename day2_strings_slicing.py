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

email= str(input("enter your email: "))

username= email[:email.index("@")]
domain = email[email.index("@")+1:]

print(username)
print(domain)