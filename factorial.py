def fact(a):
    if a == 1:
        return a
    else:
        return a*fact(a-1)
num=int(input("Enter your number: "))
if num < 0:
    print("Sorry, number is negative.")
elif num == 0:
    print("Sorry, there are no factorials for this number.")
else:
    print("The factorial of your number is = ", fact(num))