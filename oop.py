class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError
        if house not in ["h","p","q","d"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        #self.patronus = patronus


    def __str__(self):
        return f"{self.name} is in {self.house}"

    #def charm(self):
     #   match self.patronus:
      #      case "Stag":
       #         return "Right Stag"
        #    case "Dog":
         #       return "Right Dog"
          #  case _:
           #     return "Nothing"

def main():
    student = get_student()
    print(student)
    #print("Expecto Petronium")
    #print(student.charm())


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
    name = input("Name: ")
    house = input("House: ")
    #patronus = input("Petronus: ")  
    return Student(name, house)                #objects are mutable but can be made immutable            
    


if __name__ == "__main__":
    main()