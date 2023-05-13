password = input()

while True:
    line = input()

    if line == "Done":
        print(f"Your password is: {password}")
        break

    line = line.split()
    command = line[0]

    if command == "TakeOdd":
        copy_pwd = password[:]
        password = ""
        for i in range(1, len(copy_pwd), 2):
            password += copy_pwd[i]
        print(password)

    elif command == "Cut":
        idx = int(line[1])
        length = int(line[2])

        password = password[:idx] + password[length + idx:]
        print(password)

    elif command == "Substitute":
        substring = line[1]
        substitute = line[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

