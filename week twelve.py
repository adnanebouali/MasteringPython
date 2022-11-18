# الدروس من رقم 086 إلى رقم 089
# Task one 
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []
final_string=""
for data in zip(my_list, my_tuple):
    final_string =final_string+''.join(data)
print(final_string) # Elzero