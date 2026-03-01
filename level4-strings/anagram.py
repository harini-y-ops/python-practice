#An anagram is when two words have the exact same letters but in different order.

str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
sorted(str1)
sorted(str2)
print(sorted(str1))
print(sorted(str2))
if sorted(str1)==sorted(str2):
    print("It is an anagram")
else:
    print("It is not an anagram")
