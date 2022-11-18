# الدروس من رقم 086 إلى رقم 089
# # Task one 
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []
# final_string=""
# for data in zip(my_list, my_tuple):
#     final_string =final_string+"".join(data)
# print(final_string) # Elzero

# Task two
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []
final_string=""
for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if item1 == str(item1):
        final_string=final_string+item1

print(final_string)