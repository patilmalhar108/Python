print("Checking a number if it is prime or not")
n=int(input("Enter a number: "))
if n>1:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(f"{n} Number is not prime.")
            break
        else:
            print(f"{n} Number is prime.")
else:
    print(f"{n} Number is not prime")