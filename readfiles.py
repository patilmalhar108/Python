file = open("code.txt",'r')
file2 = open("code2.txt",'w')

for line in file.readlines():
    if not(line.startswith('Coding')):
        print(line)
        file2.write(line)
file.close()
file2.close()