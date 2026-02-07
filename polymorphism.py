class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("I am a cat. My name is:", {self.name})
        print("My age is:", {self.age})
    def sound(self):
        print("Meow")
class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print("I am a dog. My name is:", {self.name})
        print("My age is:", {self.age})
    def sound(self):
        print("Bark")
cat1 = cat("Kitty",3)
dog1 = dog("Spot",5)
for animal in(cat1,dog1):
    animal.sound()
    animal.info()