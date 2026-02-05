class Expression:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add_three_numbers(self):
        result = self.num1 + self.num2 + self.num3
        print("Addition result:", result)


# Creating objects and calling the method
exp1 = Expression(10, 20, 30)
exp1.add_three_numbers()   # Addition result: 60

exp2 = Expression(5, 7, 3)
exp2.add_three_numbers()   # Addition result: 15