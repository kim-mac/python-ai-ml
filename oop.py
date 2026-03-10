class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} is in {student.house}")


def get_student():
    #name = input("enter name: ")
    #house = input("enter house: ")
    #return name,house              #this is a tuple (it is immutable i.e value cannot be changed),it can also be a list inwhich values can be changed


    #method 2 using dictionary
    #student = {}
    #student["name"] = input("Name: ")
    #student["house"] = input("House: ")  #dictionary is mutable as well
    #return student

    #method 3 using class and objects
    student = Student()                #objects are mutable but can be made immutable
    student.name = input("Name: ")
    student.house = input("House:")              
    return student


if __name__ == "__main__":
    main()