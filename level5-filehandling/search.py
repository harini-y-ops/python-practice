#Search for specific word in file 
word = input("Enter a word to search: ")
with open("names.txt", "r") as f:
    for line in f:
        if word in line:
            print(f"Found: {line}")
