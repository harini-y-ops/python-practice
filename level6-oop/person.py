class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =age
    
    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} is an adult")
        else:
            print(f"{self.name} is not an adult")


name = input("Enter name: ")
age = int(input("Enter age: "))
p1 = Person(name, age)
p1.is_adult()

