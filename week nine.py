# # task One
# values = (0, 1, 2)

# if any(values):  # if there at least one true element

#     my_var = 0

# my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

# if (
#     all(my_list[:4]) or all(my_list[:6]) or all(my_list[:])
# ):  # if all the element are true

#     print("Good")

# else:

#     print("Bad")
# # good
# # task two
# v = 40

# my_range = list(range(v))

# print(sum(my_range, v) + pow(v, v, v))  # 820

# # task three
# n = 20
# l = list(range(n))
# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

#     print("Good")

# # Output => Good

## Task three
# def my_all(elements):

#     for element in elements:
#         if bool(element) != True:
#             x = False
#             break
#         else:
#             x = True
#     return x


# print(my_all([1, 2, 3]))  # True
# print(my_all([1, 2, 3, []]))  # False


# def my_any(elements):

#     for element in elements:
#         if bool(element) == True:
#             x = True
#             break
#         else:
#             x = False
#     return x


# print(my_any([(), (), [], 1]))  # True
# print(my_any([(), 0, False]))  # False


# def my_min(elements):
#     min = 0
#     for element in elements:
#         if element < min:
#             min = element
#     return min


# print(my_min([10, 100, -20, -150, 50]))  # -150
# print(my_min((10, 100, -20, -100, 50)))  # -100


def my_max(elements):
    max = 0
    for element in elements:
        if element > max:
            max = element
    return max


print(my_max([10, 100, -20, -100, 50, 700]))  # 700
print(my_max((10, 100, -20, -100, 50, 2000)))  # 2000
