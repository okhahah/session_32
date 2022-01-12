class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age = age

stud = Student("me",14)
#retriving age using getter method
print("Name",stud.name,stud.get_age())
#changing the age using setter method
stud.set_age(97)
print("Name",stud.name,stud.get_age())
