""" Assignments For Lessons 86 To 89 / Task 5"""
# Task five
my_friends = ["Ahmed", "Osama", "Sayed"]
def say_hello(some_peoples) -> list:
    """Print Hello to any one in my_friends list"""
    for someone in some_peoples:
        print(f"Hello {someone}")
say_hello(my_friends)
