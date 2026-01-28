print("List to Dictionary")
print("Create a list with 5 students. Details are: Role number, name, and grade. Then convert this list into a dictionary.")
def test(lst):
    resualt = {}
    for item in lst:
        resualt[item[0]] = item[1:]
    return resualt
students = [[1,"John",7],[2,"David",7],[3,"Phil",7],[4,"Mike",7],[5,"Chris",7]]
print("Original List")
print(students)
print("Converted list to a Dictionary")
print(test(students))