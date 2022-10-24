import os

for num in range(1, 11):
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
