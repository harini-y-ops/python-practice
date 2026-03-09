#Using list comprehension, create a list of length of each word.
sentence = "python is very powerful"
word=sentence.split()
length=[len(word) for word in word]
print(length)
