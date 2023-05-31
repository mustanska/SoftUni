import os

root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path, "Text Files", "numbers.txt")

with open(file_path, "r") as file:
    numbers = [int(x) for x in file.read().split("\n")]

print(sum(numbers))
