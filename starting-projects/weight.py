# Project for converting user input weight from Kg to Lbs and vice versa.

weight = int(input("Weight: "))

unit = input("(K)g or (L)b: ")

if unit.upper() == "K":
    converted = (weight / 0.45)
    print("Weight in Lbs: " + str(converted))

else:
    converted = (weight * 0.45)
    print("Weight in Kgs: " + str(converted))
