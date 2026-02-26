print("Program to show linier time complexity by entering any input: ")
def ontime(n):
    iteration = 0
    for i in range(n):
        iteration = iteration+1
    print("When input is:", n, "Iteration is =", iteration)
ontime(10)
ontime(20)
ontime(30)