import os

for num in range(1, 11):
    if num == 5:
        file = open(r"D:\my files\Python\MasteringPython-\assign\special-text", "w")
        num += 1
    file = open(rf"D:\my files\Python\MasteringPython-\assign\text {num}", "w")
    file.write(f"Elzero Web School => {num}")

print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
