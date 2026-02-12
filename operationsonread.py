file = open("code.txt",'r')
print(file.read())
file.close()

file2 = open("code.txt",'r')
print("\nRead file in parts\n")
print(file2.read(10)) 
file2.close()

file3 = open("code.txt",'a')
file3.write("\nCoding is very easy!\n")
file3.close()