import random

# task one
# print(f"Random Number Between 10 And 50 => {random.randint(10, 50)}")
# print(f"Random Even Number Between 2 And 10 => {random.randrange(2, 10,2)}")
# print(f"Random Odd Number Between 1 And 9 => {random.randrange(1, 9,2)}")


# import my_mod

# my_mod.say_hello()
# my_mod.say_welcome()


# from my_mod import say_welcome

# say_welcome()

# from my_mod import say_welcome as new_welcome

# new_welcome()

print("-" * 50)

import datetime

# date = datetime.datetime(1999, 5, 17)
# nowd = datetime.datetime.now()
# print(f"Days From {date} To {nowd} Is => {(nowd - date).days} Days")


nowd = datetime.datetime.now().strftime("%Y-%m-%d")
print(nowd)
nowd = datetime.datetime.now().strftime("%b %d,%Y")
print(nowd)
nowd = datetime.datetime.now().strftime("%d - %b - %Y")
print(nowd)
nowd = datetime.datetime.now().strftime("%d / %b / %y")
print(nowd)
nowd = datetime.datetime.now().strftime("%d / %B / %Y")
print(nowd)
nowd = datetime.datetime.now().strftime("%a, %d  %B  %Y")
print(nowd)
