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
