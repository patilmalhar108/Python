print("Program to find HCF")
largest = int(input("Enter your largest number: "))
smallest = int(input("Enter your smallest number: "))

while smallest:
    number_store = smallest
    smallest = largest % smallest
    largest = number_store

print("HCF is =",largest)