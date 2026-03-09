#Filter words longer than 4 letters
words = ["python","java","ai","machine","code","data"]
new=[word for word in words if len(word) > 4]
print(new)
