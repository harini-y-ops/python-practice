class Animal:
    def __init__(self,name):
        self.name=name
     
    def speak(self):
        print(f"{self.name} makes a sound")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says WOOF")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says MEOW")
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")
        
        
d1=Dog("Bruno")
d2=Cat("Mellissa")
d3=Bird("Chirp")
d1.speak()
d2.speak()
d3.fly()

