#Count word frequency
str1=input("Enter the sentence: ")
for vowel in "aeiouAEIOU":
    str1=str1.replace(vowel,"*")
print(str1)
