# ask for user input and append 
new_name = input("Enter a new name to add: ")
with open("names.txt", "a") as f:
    f.write(new_name + "\n")
print(f"{new_name} added successfully!")
