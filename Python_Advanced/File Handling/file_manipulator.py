import os

root_path = os.path.dirname(os.path.abspath(__file__))

while True:
    command, *file_info = input().split("-")

    if command == "End":
        break

    file_path = os.path.join(root_path, file_info[0])

    if command == "Create":
        with open(file_path, "w") as file:
            file.seek(0)

    elif command == "Add":
        content = file_info[1]

        with open(file_path, "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        old_string = file_info[1]
        new_string = file_info[2]

        try:
            with open(file_path, "r+") as file:
                text = file.read().replace(old_string, new_string)
                file.seek(0)
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("An error occurred")
