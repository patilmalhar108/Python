with open("hello.txt",'w') as file:
    file.write("Welcome to coding")
file.close()

with open("hello.txt",'r') as file:
    data = file.readlines()
    print("Sentance has been converted to words: ")
    for line in data:
        word = line.split()
        print(word)
file.close()