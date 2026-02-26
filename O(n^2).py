print("Program to show the time complexity O(n^2) by taking n input: ")
def onsquaretime(n):
    iteration = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end = " ")
            iteration = iteration+1
        print("")
    print("When n is =", n, "Iteration is =", iteration)

onsquaretime(10)
onsquaretime(20)
onsquaretime(30)
print("With every n, the time taken = n^2")
print("O(n^2)")