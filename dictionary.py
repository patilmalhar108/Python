print("Operations on Dictionary")
dict = {}
dict = {1:"Apple",2:"Banana"}
dict = {"Name":"Jim",1:[2,4,3]}
dict = {"Name":"Steve","Age":25}
print(dict["Name"])
print(dict.get("Age"))
dict["Address"] = "532 Chicago"
print(dict)
print("Address: ", dict.get("Address"))
#dict.clear()
print(dict)