print("Take the roman numerial from the user and change it to integer")
def roman_to_int(roman_input):
    roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X': 10, 'V':5, 'I':1}
    result = 0

    for i in range(0,len(roman_input)-1):
        if roman[roman_input[i]] < roman[roman_input[i+1]]:
            result -= roman[roman_input[i]]
        else:
            result += roman[roman_input[i]]
    return result + roman[roman_input[-1]]
roman = input("Input roman numerial: ")
print("Interger equaliant:",roman_to_int(roman))