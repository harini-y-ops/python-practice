# Write all these names to a file called names.txt — one name per line!
names=["Harini","Vignesh","Noor","Akshatha","Soya"]
with open ("names.txt","w")as f:
    for name in names:
        f.write(name+"\n")
print("file written successfully")
