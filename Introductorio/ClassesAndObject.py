
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def view(self):
        print(self.name)



