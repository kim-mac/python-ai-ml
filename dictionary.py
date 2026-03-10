student = {"name":"Kim","Major":"IS","Courses":["Math","Sci"],"age":25}

#student["phone"]= 555555555                                   #to add new data

#student["name"] = "Baby"                                      #one way to update data
student.update({"name":"Bhairavi","Courses":["Bio","PH"]})     #another way to update data all at once

for key,value in student.items():                              #to loop through the dictionary if we dont use items we will just get keys
    print(key, value)

#del student["name"]            #delete some data
#name = student.pop("name")     #can remove the desired value and return it
student.popitem()                 #removes the last item

print(student.get("Major"))       #can get values and if a value isnt present returns none

print(student)
#print(name)
print (len(student))    #gives length of the dictionary key-value =1
print(student.keys())  #gives keys of the dictionary
print(student.values())  #gives values of the dictionary
print(student.items())  #gives key value pairs

