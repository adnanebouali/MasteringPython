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


# # task three
# def show_skills(name, *skills):
#     if skills == ():
#         print(f"Hello {name} You Have No Skills To Show")
#     else:
#         print(f"Hello {name} Your Skills Are : ")
#         for skill in skills:
#             print(f"- {skill}")


# show_skills("Osama", "HTML", "CSS", "JS", "Python")
# show_skills("Ahmed")


# def say_hello(name="unknown", age="unknown", country="unknown"):
#     return f"Hello {name} Your Age Is {age} And You Live In {country}"


# print(say_hello("Osama", 38, "Egypt"))
# print(say_hello())

# # Task one
# def get_score(**scores):
#     for subject, score in scores.items():
#         print(f"{subject} => {score}")


# get_score(Math=90, Science=80, Language=70)
# get_score(Logic=70, Problems=60)

# Task two

def get_people_scores(name="", **skills):
    if skills == {}:
        print(f"Hello {name} You Have No Scores To Show")
    else:
        if name != "":
            print(f"Hello {name} This Is Your Score Table:")
        for skill, progress in skills.items():
            print(f"{skill} => {progress}")


get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")
