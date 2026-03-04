class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    
    def introduce(self):
        print(f"Hi I am {self.name} and I am {self.age} years old")
    def show_grade(self):
        print(f"{self.name} has scored {self.grade}.")

s1 = Student("Harini", 20, "A")
s2=Student("Janani",21,"A")
s3=Student("Amulya",22,"A+")
s1.show_grade()
s2.show_grade()
s3.show_grade()
