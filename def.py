#open the file in read mode
d = open("abc.txt",'r')
print("File is at read mode")
print(d.read())
d.close()
#open the file in write mode
e = open("abc.txt",'w')
e.write("Hello world")
e.close()
#open the file in append mode
f = open("abc.txt",'a')
f.write("I like sports")
f.write("My favorite is baseball")
print(f.read())