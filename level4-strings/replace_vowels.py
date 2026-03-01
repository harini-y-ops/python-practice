#Replace vowels with *
str1 = input("Enter the sentence: ")
for vowel in "aeiou":
    str1 = str1.replace(vowel, "*")
print(str1)
