#squares of even numbers from 1 to 10 
num=range(1,21)
square_even=[num**2 for num in range (1,11) if num%2==0]
print(square_even)
