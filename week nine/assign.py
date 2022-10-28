import os

for num in range(1, 51):
    if num == 5:
        file = open(r"D:\my files\Python\MasteringPython-\assign\special-text.txt", "w")
        num += 1
    file = open(rf"D:\my files\Python\MasteringPython-\assign\txt{num}.txt", "w")
    file.write(f"Elzero Web School => {num}")

print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))

fileone = open(r"D:\my files\Python\MasteringPython-\assign\txt1.txt", "a")
fileone.write("\n")
fileone.write("Appended => Elzero Web School\n" * 50)

fileone = open(r"D:\my files\Python\MasteringPython-\assign\txt1.txt")
print(len(fileone.readlines()))
fileone = open(r"D:\my files\Python\MasteringPython-\assign\txt1.txt")
char = 0
wor = 0
lett = 0
for word in fileone.read():
    char += 1
    if word == ">":
        char -= 1
    if word == " ":
        wor += 1
        char -= 1
    if word == "l":
        lett += 1
print(wor + 51)
print(char)
print(lett)
file.close()
for r in range(-50, -40):
    r = r * -1
    os.remove(rf"D:\my files\Python\MasteringPython-\assign\txt{r}.txt")
