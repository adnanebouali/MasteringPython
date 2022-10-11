# Task one
num = int(input("enter a number: "))
if num > 0:
    som = 0
    while num != 1:
        num -= 1
        if num == 6:
            continue
        print(num)
        som += 1
    print(f"total number printed is {som}")
else:
    print("The number you entered is smaller than 0")
print("-"*30)
# task two
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
i = 0
som = 0
while i < len(friends):
    if friends[i] == friends[i].lower():
        i += 1
        som += 1
        continue
    print(friends[i])
    i += 1
print(f"Friends Printed And Ignored Names Count Is {som}")
print("-"*30)
