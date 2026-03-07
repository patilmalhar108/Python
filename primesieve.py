print("Implantation of Sieve of Eratosthene")
def soe(number):
    prime = [True for i in range(number+1)]
    p = 2
    while (p * p <= number):
        if prime[p] == True:
            for i in range(p * p, number + 1, p):
                prime[i] = False
        p = p + 1
    for p in range(2,number + 1):
        if prime[p]:
            print(p)

number = int(input("Enter your number: "))
print("Following are the prime numbers smaller or equal to",number,": ")
soe(number)