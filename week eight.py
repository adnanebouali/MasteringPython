# # task one
# def calculate(num1, num2, op="add"):
#     op = op.lower()
#     if op == "add" or op == "a":
#         return num1+num2
#     elif op == "subtract" or op == "s":
#         return num1-num2
#     elif op == "multiply" or op == "m":
#         return num1*num2
#     else:
#         return "Op unknown"

# print(calculate(10, 20))  # 30
# print(calculate(10, 20, "AdD"))  # 30
# print(calculate(10, 20, "a"))  # 30
# print(calculate(10, 20, "A"))  # 30

# print(calculate(10, 20, "S"))  # -10
# print(calculate(10, 20, "subTRACT"))  # -10

# print(calculate(10, 20, "Multiply"))  # 200
# print(calculate(10, 20, "m"))  # 200

# # task two

# def addition(*nums):
#     som = 0
#     for n in nums:
#         if n == 10:
#             continue
#         som += n
#         if n == 5:
#             som = som - 5
#     return som


# print(addition(10, 20, 30, 10, 15))  # 65
# print(addition(10, 20, 30, 10, 15, 5, 100))  # 165
# task three

from queue import Empty
from re import S


def show_skills(name, *skills):
    if skills == ():
        print(f"Hello {name} You Have No Skills To Show")
    else:
        print(f"Hello {name} Your Skills Are : ")
        for skill in skills:
            print(f"- {skill}")


show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")
