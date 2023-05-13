capacity_msg = int(input())

users = {}

while True:
    line = input()

    if line == "Statistics":
        break

    line = line.split("=")
    command = line[0]

    if command == "Add":
        username = line[1]
        sent = int(line[2])
        received = int(line[3])

        if username in users:
            continue

        users[username] = {"sent": sent, "received": received}

    elif command == "Message":
        sender = line[1]
        receiver = line[2]

        if sender in users and receiver in users:
            users[sender]["sent"] += 1
            users[receiver]["received"] += 1

            if users[sender]["sent"] + users[sender]["received"] >= capacity_msg:
                del users[sender]
                print(f"{sender} reached the capacity!")

            if users[receiver]["sent"] + users[receiver]["received"] >= capacity_msg:
                del users[receiver]
                print(f"{receiver} reached the capacity!")

    elif command == "Empty":
        username = line[1]

        if username == "All":
            users.clear()
            continue

        if username in users:
            del users[username]

print(f"Users count: {len(users)}")
for user, values in users.items():
    sum_msg = values["sent"] + values["received"]

    print(f"{user} - {sum_msg}")