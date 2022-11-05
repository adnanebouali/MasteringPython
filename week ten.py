# Task one
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]


def remove_chars(name):
    return name[1:-1:]


cleaned_list = map(remove_chars, friends_map)
for name in cleaned_list:
    print(name)

# lambda
cleaned_list_lambda = map(lambda name: name[1:-1:], friends_map)
for name in cleaned_list_lambda:
    print(name)

# Task two
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]


def get_names(name):
    return name[-1] == "m"


print()
names = filter(get_names, friends_filter)

for nameM in names:
    print(nameM)

# lambda
for nameM in filter(lambda name: name[-1] == "m", friends_filter):
    print(nameM)

# task three
from functools import reduce

nums = [2, 4, 6, 2]


def mul(num1, num2):
    return num1 * num2


reslt = reduce(mul, nums)
resltLambda = reduce(lambda num1, num2: num1 * num2, nums)
print(reslt)
print(resltLambda)

# task four
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
skills = reversed(skills)
skills = enumerate(skills, 50)
for counter, skill in skills:
    if type(skill) == int:
        pass
    else:
        print(f"{counter} - {skill}")
