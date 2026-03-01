#Check if a number is a palindrome
num=str(input("Enter a number: "))
reversed_num=num[::-1]
print(f"Reversed Number={reversed_num}")
if num==reversed_num:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
