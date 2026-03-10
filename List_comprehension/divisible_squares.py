#Squares of numbers divisible by 3 or 5
# list of squares of numbers from 1–30 that are divisible by 3 OR 5.
Create anum=range(1,31)
div=[x**2 for x in range(1,31) if x%3==0 or x%5==0]
print(div)
