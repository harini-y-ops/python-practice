#Find the largest between two numbers 
num1=int(input("Enter a number 1: "))
num2=int(input("Enter the second number: "))
if(num2>num1):
    print("num2 is greater: ",num2)
elif(num1>num2):
    print("num 1 is greater: ", num1)
else:
    print("Both are equal")
