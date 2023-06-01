import os


def directory_traversal(path, level=0):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isdir(file_path):
            directory_traversal(file_path, level + 1)

        elif os.path.isfile(file_path):
            extension = file.split(".")[-1]

            if extension not in files:
                files[extension] = []

            files[extension].append(file)

        elif level == 1:
            break


directory = input()

files = {}

directory_traversal(directory)

with open(os.path.join(directory, "report.txt"), "w") as report_file:
    for key, values in sorted(files.items()):
        result = f".{key}\n"
        result += "".join([f"- - - {file}\n" for file in sorted(values)])
        report_file.write(result)
