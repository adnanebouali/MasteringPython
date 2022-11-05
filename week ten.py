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
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]


def get_names(name):
    return name[-1] == "m"


names = filter(get_names, friends_filter)

for nameM in names:
    print(nameM)

# lambda
for nameM in filter(lambda name: name[-1] == "m", friends_filter):
    print(nameM)
