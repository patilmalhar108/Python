import os
newfile = open("ghi.txt",'x')
newfile.close()
print("Checking if my file exists or not")
if os.path.exists("ghi.txt"):
    os.remove("ghi.txt")
else:
    print("This file does not exist")