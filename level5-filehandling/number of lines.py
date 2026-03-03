# Count number of lines in a file 
names=["Harini","Vignesh","Noor","Akshatha","Soya"]
with open("names.txt","r")as f:
    lines=f.readlines()
    print(f"The number of lines are {len(lines)}")
