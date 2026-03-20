#exercise 1 convert weight to pounds and vice versa

weight=int(input("Enter your weight:"))
unit=input("Enter your unit:")

if unit=="kg":
    converted_weight=weight/0.45
    print("your weight in pound is ",converted_weight)
elif unit=="lb":
    converted_weight=weight*0.45
    print("your weight in kg is ",converted_weight)
else:
    print("enter a valid unit")