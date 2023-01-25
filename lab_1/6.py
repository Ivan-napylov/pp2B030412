age = int(input())
paym = int(input())
vis = bool(input())


if (11 <= age and age <= 12 and paym >= 900 and vis == True):
    print("Allowed")
elif (13 <= age and age <= 16 and paym >= 900):
    print("Allowed")
elif (17 <= age and age <= 22 and paym >= 1400):
    print("Allowed")
elif (age >= 22 and paym >= 1900):
    print("Allowed")
else: 
    print("Not allowed")
