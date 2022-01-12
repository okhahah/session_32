class Student:
    def __init__(self):
        self._age = 0

    def get_age(self):
        print("Getter method is called")
        return self._age
    
    def set_age(self,a):
        print("Setter method is called")
        self._age = a

    def del_age(self):
        del self._age

    age = property(get_age,set_age,del_age)


stud = Student()
stud.age = 99
print(stud.age)
        
