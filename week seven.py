# # Task one
# num = int(input("enter a number: "))
# if num > 0:
#     som = 0
#     while num != 1:
#         num -= 1
#         if num == 6:
#             continue
#         print(num)
#         som += 1
#     print(f"total number printed is {som}")
# else:
#     print("The number you entered is smaller than 0")
# print("-"*30)
# # task two
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
# i = 0
# som = 0
# while i < len(friends):
#     if friends[i] == friends[i].lower():
#         i += 1
#         som += 1
#         continue
#     print(friends[i])
#     i += 1
# print(f"Friends Printed And Ignored Names Count Is {som}")
# print("-"*30)
# Task Three
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
# while skills:
#     print(skills.pop())

# # Task four
# my_friends = []
# limit = 4
# while limit > 0:
#     name = input("Add member to the list : ").strip()
#     if name.upper() == name:
#         print("Invalid Name")
#     else:
#         my_friends.append(name.capitalize())
#         limit -= 1
#         print(f"Friend {name} Added\nNames Left in List are {limit}")
# print(my_friends)

# # Task one 2
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# print(my_nums)
# for num in my_nums:
#     if num % 5 == 0:
#         print(num)
# print("All Numbers Printed")
# # Task two 2
# for i in range(1, 21):
#     if i in [6, 8, 10]:
#         continue
#     print(str(i).zfill(2))
# print("Done")
# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }
# for rank in my_ranks:
#     print(
#         f"My Rank in {rank} Is {my_ranks[rank]} And This Equal 100 Points" if my_ranks[rank] == "A" else f"My Rank in {rank} Is {my_ranks[rank]} And This Equal 80 Points" if my_ranks[rank] == "B" else f"My Rank in {rank} Is {my_ranks[rank]} And This Equal 40 Points")
# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }
# som = 0
# for rank in my_ranks:
#     if my_ranks[rank] == "A":
#         som += 100
#         print(
#             f"My Rank in {rank} Is {my_ranks[rank]} And This Equal 100 Points")
#     elif my_ranks[rank] == "B":
#         som += 80
#         print(
#             f"My Rank in {rank} Is {my_ranks[rank]} And This Equal 80 Points")
#     else:
#         som += 40
#         print(
#             f"My Rank in {rank} Is {my_ranks[rank]} And This Equal 40 Points")
# print(f"Total Points Is {som}")

# Task three
students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}


for student in students:
    som = 0
    print("-"*30)
    print(student.center(30, "-"))
    print("-"*30)
    for skill in students[student]:
        if students[student][skill] == "A":
            som += 100
            print(
                f"{skill} ==> 100 Points")
        elif students[student][skill] == "B":
            som += 80
            print(
                f"{skill} ==> 80 Points")
        elif students[student][skill] == "C":
            som += 40
            print(
                f"{skill} ==> 40 Points")
        else:
            som += 20
            print(
                f"{skill} ==> 20 Points")
    print(f"Total Points Is {som}")
