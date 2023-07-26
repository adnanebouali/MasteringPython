# task one
print(bool(True))
print(bool("adnane"))
print(bool(200))
print(bool(200.00))
print(bool(""))
print(bool(False))
print(bool({}))
print(bool([]))
print("-" * 50)
# task two
html = 80
css = 60
javascript = 70
print(html > 50 and css > 50 and javascript > 50)
print("-" * 50)
# task three
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)
print("-" * 50)
# task four
num_one = 10
num_two = 20
result = num_one + num_two
print(result)
print(result**3)
print((result**3) % 2600)
print(((result**3) % 2600) / 5)
print(type(str(((result**3) % 2600) / 5)))

print("=" * 50)
# Task one
name = input("Enter your name: ").strip().capitalize()
print(name)
print("-" * 50)

# Task two
Age = int(input("Enter your Age: "))
if Age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {Age}, All Articles Is Suitable For You")
print("-" * 50)

# Task three
fname = input("Enter your First Name: ").strip().capitalize()
lname = input("Enter your Last Name: ").strip().capitalize()
print(f"Hello {fname} {lname[0]}.")
print("-" * 50)

# Task four
email = input("Enter your email: ").strip().lower()
name = email[: email.index("@")]
domain = email[email.index("@") + 1 : email.index(".")]
top_domain = email[email.index(".") + 1 :]
print(f"Your Name Is {name}")
print(f"Email Service Provider Is {domain}")
print(f"Top Level Domain Is {top_domain}")
