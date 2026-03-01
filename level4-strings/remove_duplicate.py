#Remove duplicate characters
str1 = input("Enter a string: ")
result = []
for char in str1:
    if char not in result:
        result.append(char)
print("".join(result))
