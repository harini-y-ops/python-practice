#print n numbers using generator 
def count_num(n):
    for i in range(1,n+1):
        yield(i)
n=int(input("Enter the number you want to count till: "))
for num in count_num(n):
    print(num)
