# Try writing a program that adds a new name to names.txt without deleting the existing names
names=["Harini","Vignesh","Noor","Akshatha","Soya"] 
with open("names.txt","a")as f: 
  f.write("Shravani\n")
