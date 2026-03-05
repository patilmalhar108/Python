print("Program to check the given number is a palindrome number or not.")
number = int(input("Enter your number: "))
original_number = number
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number //= 10

if original_number == reverse_number:
    print("The given number is a palindrome number")
else:
    print("The given number is not a palindrome number")