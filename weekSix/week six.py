# Task One
num_one = int(input("Enter the First number : ").strip())
num_two = int(input("Enter the Second number : ").strip())
op = input("choose your operation '+ , - , * , / , % ' ").strip().lower()
if op == "+":
    print(f"{num_one} + {num_two} = {num_one+num_two}")
elif op == "-":
    print(f"{num_one} - {num_two} = {num_one-num_two}")
elif op == "*":
    print(f"{num_one} * {num_two} = {num_one*num_two}")
elif op == "/":
    print(f"{num_one} / {num_two} = {num_one/num_two}")
elif op == "%":
    print(f"{num_one} % {num_two} = {num_one%num_two}")
else:
    print("operation is not available")
print("-"*50)
# task two
age = int(input("enter your age : ").strip())
print("App Is Suitable For You" if age > 16 else "App Is not Suitable For You")
print("-"*50)
# Task three
age = int(input("enter your age : ").strip())
months = age*12
weeks = months*4
days = age*365
minutes = days*60
seconds = minutes*60
if age > 10 and age < 100:
    print(f"Your Age In Months Is {months:,} Month")
    print(f"Your Age In weeks Is {weeks:,} week")
    print(f"Your Age In days Is {days:,} day")
    print(f"Your Age In minutes Is {minutes:,} minute")
    print(f"Your Age In seconds Is {seconds:,} second")
else:
    print("The age is out of range")
print("-"*50)
# task four
country = input("Input Your Country: ").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria",
             "Yemen", "Ksa", "Usa", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    print(
        f"Your Country Eligible For Discount And The Price After Discount Is {price - discount}")
else:
    print(
        "Your Country Not Eligible For Discount And The Price Is {:d}".format(price))
