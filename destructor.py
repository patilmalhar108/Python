print("Destructor")
class employ:
    def __init__(self):
        print("Employ created")
    def __del__(self):
        print("Destructor called; employ deleted") 
obj = employ()
del obj        