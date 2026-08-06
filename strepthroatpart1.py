#Strep Throat(a) = 20%, Does not have Strep Throat = 80%
#Positive result with Strep Throat(b) = 85%, Negative result with Strep Throat = 15%
#Postitive result without Strep Throat = 2%, Negative result without Strep Throat = 98%
def find_prob(a,b):
    if a == 1:
        prob_a = 0.2
        if b == 1:
            prob_bga = 0.85
        elif b == 2:
            prob_bga = 0.15
        else:
            print("Invalid Choice")
        prob_a_b = prob_a * prob_bga
        print("Probability of both events:", prob_a_b)
    elif a == 2:
        prob_a = 0.8
        if b == 1:
            prob_bga = 0.02
        elif b == 2:
            prob_bga = 0.98
        else:
            print("Invalid Choice")
        prob_a_b = prob_a * prob_bga
        print("Probabilty of both events:", prob_a_b)
    else:
        print("Invalid Choice")

print("Lets calculate probability")
print("Person has Strep Throat\n1: Yes\n2: No")
a = int(input("Enter your choice 1 or 2: "))
print("Person has tested positive?\n1: Yes\n2: No")
b = int(input("Enter your choice 1 or 2: "))
print("Probability of event a and b:", find_prob(a,b))