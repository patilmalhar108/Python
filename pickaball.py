import random

def pick_ball():
    balls = ['Red', 'Blue', 'Yellow']
    pick = random.choice(balls)
    prob = balls.count('Red')/len(balls)
    print("Probability of red ball is:", prob)
    if pick == 'Red':
        print("Red ball was selected")
    else:
        print("Red ball was not selected")

res = pick_ball()
print(res)