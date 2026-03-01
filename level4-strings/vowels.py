#Count how many vowels are present in a string.
str1=input("Enter a string: ")
count=0
for char in str1:
    if char in "aeiou":
        count+=1
print(f"The number of vowels are {count}")
