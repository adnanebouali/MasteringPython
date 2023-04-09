# task one
n, a, c = "Adnane", "23", "Algeria"
print("Hello '" + n + "', How Are You Doing \\ \"\"\" Your Age Is \"" +
      a + "\"\" + and your country is:", c)

# task two
print("Hello '" + n + "', How Are You Doing \\ \n \"\"\" Your Age Is \"" +
      a + "\"\" + \n and your country is:", c)

# task three
name = "elzero"
print(name[1])
print(name[2])
print(name[-1])


# task four
name = "Elzero"
print(name[1:4])
print(name[::2])
print(name[4::-2])
# Needed Output
# "lze"
# "Ezr"
# "rzE"

# task five
name = "#@#@Elzero#@#@"
print(name.strip("#@"))

# task six
a, b, c, d, e = "1", "11", "111", "1111", "11111"
print(a.zfill(5))
print(b.zfill(5))
print(c.zfill(5))
print(d.zfill(5))
print(e.zfill(5))

# task seven
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

# task eight
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())

# task nine
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

# task ten
name = "Elzero"
print(name.find("z"))

# task eleven
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1))

# task twelve
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love"))

# task thirteen
Name, Age, Country = "Adnane", 23, "Algeria"
print("my name is %s my age is %d Mycountry is %s" % (Name, Age, Country))
print("my name is {} my age is {} Mycountry is {}" .format(Name, Age, Country))
print("my name is {:s} my age is {:d} Mycountry is {:s}" .format(
    Name, Age, Country))
print(f"my name is {Name} my age is {Age} Mycountry is {Country}")
