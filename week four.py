# Task one
from unicodedata import name


my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
my_list = list(unique_list)
print(my_list)
print(type(my_list))
print(my_list[:-1])

# Task Two
nums = {1, 2, 3}
letters = {"A", "B", "C"}
res = nums.union(letters)
nums.update(letters)
print(nums | letters)
print(res)
print(nums)


# Task Three
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C")

# Task Four
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))

# Task Five
MyLang = {
    "L1": {
        "name": "HTML",
        "progress": "90%"
    },
    "L2": {
        "name": "CSS",
        "progress": "80%"
    },
    "L3": {
        "name": "JS",
        "progress": "30%"
    }
}
print("{} Progress is {}".format(
    MyLang["L1"]["name"], MyLang["L1"]["progress"]))
print("{} Progress is {}".format(
    MyLang["L2"]["name"], MyLang["L2"]["progress"]))
print("{} Progress is {}".format(
    MyLang["L3"]["name"], MyLang["L3"]["progress"]))
