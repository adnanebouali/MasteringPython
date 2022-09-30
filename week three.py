# task one
print(3)
print(3.5)
print(3+5j)

# task two
val = 3+2j
print("real num is:{}".format(val.real))
print("imaginary num is:{}".format(val.imag))

# task three
num = 10
print(format(num, ".10f"))

# task four
num2 = 159.650
print(int(num2))
print(type(int(num2)))

# task five
print(100 - 115)
print(50 * 30)
print(21 % 4)
print(110 // 11)
print(97 // 20)


# Two
# task one
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-1])

# task two
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1::2])

# task three
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[-2:])

# task four
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[3:] = "1", "1"
print(friends)

# task five
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends.insert(0, "adnane")
friends.insert(6, "adnane")
print(friends)

# task six
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
del friends[0:2]
print(friends)
del friends[-1]
print(friends)

# task seven
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

# task eight
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)

# task nine
print(len(friends))

# task ten
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][-1])
