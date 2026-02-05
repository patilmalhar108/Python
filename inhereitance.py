print("Inheritance") 
class dad:
    def __init__(self,eyes,aggresion):
        self.eyes = eyes
        self.aggresion = aggresion
    def display(self):
        print("Your eye colors are: ",self.eyes)
        print("You are aggresive: ", self.aggresion)
class child(dad):
    def __init__(self,name,age,eyes,aggresion):
        self.name = name
        self.age = age
        dad.__init__(self,eyes,aggresion)
obj = child("Penguin",5,"Brown",True)
obj.display()