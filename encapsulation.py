print("Encapsulation")
print("Make the attribute private")
class computer:
    def __init__(self):
        self.__maxprice = 900
    def self(self):
        print("Selling price{}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice = price
c = computer()
c.self()
c.setmaxprice(1000)
c.self()