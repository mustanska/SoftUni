import os

root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path, "Text Files", "text.txt")

if os.path.isfile(file_path):
    print("File found")
    open(file_path, "r")
else:
    print("File not found")