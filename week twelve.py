# الدروس من رقم 086 إلى رقم 089
# # Task one 
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []
# final_string=""
# for data in zip(my_list, my_tuple):
#     final_string =final_string+"".join(data)
# print(final_string) # Elzero

# # Task two
# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []
# final_string=""
# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
#     if item1 == str(item1):
#         final_string=final_string+item1

# print(final_string)


# Task Three

from PIL import Image, ImageOps
my_image=Image.open(r"D:\my files\Python\MasteringPython-\elzero-pillow.png")
# my_image.show()
# box=(400,0,800,400)
# croped_image=my_image.crop(box)
# croped_image.show()
# gray_image = ImageOps.grayscale(croped_image)
# gray_image.show()
# box_two=(0,400,1200,800)
# croped_image_two=my_image.crop(box_two)
# croped_image_two.show()
# gray_image_two = ImageOps.grayscale(croped_image_two).rotate(180)
# gray_image_two.show()

# Task four
def say_hello_to(name):
    """
    parameter(someone) => Person Name
    Function To Say Hello To Anyone
    """
    return "Hello %s" %(name)

print(say_hello_to("Osama"))
print(say_hello_to.__doc__)
help(say_hello_to)