file = open("code.txt",'r')
file2 = open("code2.txt",'w')
content = file.readlines()
type(content)
for i in range(1,len(content)+1):
    if (i%2 != 0):
        file2.write(content[i-1])
    else:
        pass
file2.close()
file2 = open("code2.txt",'r')
content1 = file2.read()
print(content1)
file.close()
file2.close()