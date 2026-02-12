file = open("code.txt",'r')
print(file.read())
file.close()

file2 = open("code.txt",'a')
file2.write("\nCoding helps in many ways!\n")
file2.close()

file3 = open("code.txt",'w')
file3.write("\nIt is very important\n")
file3.close()