#Numbers divisible by 4
#Create a list of numbers between 1 and 30 that are divisible by 4.
num=range(1,31)
numbers=[num for num in range(1,31) if num%4==0]
print(numbers)
