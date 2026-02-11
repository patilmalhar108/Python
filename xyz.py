x = open("abc.txt",'r')
counter = 0
content = x.read()
CoList = content.split("\n")
for i in CoList:
    if i:
        counter = counter+1
print(counter)