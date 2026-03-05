print("Program to find LCM")
#import math
#number1 = int(input("Enter your first number: "))
#number2 = int(input("Enter your second number: "))
#result = math.lcm(number1, number2)
#print("LCM is equal to", result)

def compute_LCM(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater = greater + 1
    return lcm
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
result = compute_LCM(number1, number2)
print(f"The LCM of {number1} and {number2} is: {result}")