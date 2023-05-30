import os

root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path, "my_first_file.txt")

if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("File already deleted!")

