# generator that yields square
def count_num(n):
    for i in range(1,n+1):
        i=i*i
        yield(i)
n=int(input("Enter the number: "))
for num in count_num(n):
    print(num)
