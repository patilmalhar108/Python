print("BMI Calculator")
height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg: "))
bmi=weight/(height/100)**2
if bmi<=18.5:
    print("You are underweight.")
elif bmi<=24.9:
    print("You are normal weight.")
elif bmi<=29.9:
    print("You are overweight.")