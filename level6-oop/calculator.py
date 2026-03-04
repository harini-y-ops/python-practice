class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        if self.num2==0:
            print("Invalid , cannot divide by 0")
        else:
            return self.num1/self.num2

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
calc=Calculator(num1,num2)
print(calc.add())
print(calc.div())

