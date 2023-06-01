import os


def add_element_in_files_dict(file_extension, file_name):
    if file_extension not in files:
        files[file_extension] = []

    files[file_extension].append(file_name)


directory = input()

files = {}

while True:
    for file_in_zero_level in os.listdir(directory):
        file_path = os.path.join(directory, file_in_zero_level)

        if os.path.isdir(file_path):
            for file_in_first_level in os.listdir(file_path):
                extension = file_in_first_level.split(".")[-1]
                add_element_in_files_dict(extension, file_in_first_level)
            break

        else:
            extension = file_in_zero_level.split(".")[-1]
            add_element_in_files_dict(extension, file_in_zero_level)

    break

with open(os.path.join(directory, "report.txt"), "w") as report_file:
    for key, values in sorted(files.items()):
        result = f".{key}\n"
        result += "".join([f"- - - {file}\n" for file in sorted(values)])
        report_file.write(result)
