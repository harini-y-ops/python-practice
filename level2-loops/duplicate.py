#Remove duplicates from a list without using set()
list=[1,2,3,4,5,1,2,7,8,2,3]
new_list=[]
for item in list:
    if item not in new_list:
        new_list.append(item)
print(new_list)
