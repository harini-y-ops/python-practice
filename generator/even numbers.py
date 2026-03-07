#print only even numbers using generators 
def count_num(n):
    for i in range(1,n+1):
        if(i%2==0):
            yield(i)
n=int(input("Enter the number: "))
for num in count_num(n):
    print(num)
