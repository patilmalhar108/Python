# Using Classes and Objects to make robots introduce themselves

class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello! My name is {self.name}.")

# Creating objects (robots)
tom = Robot("Tom")
jerry = Robot("Jerry")

# Making the robots introduce their names
tom.introduce()
jerry.introduce()