first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

commands = {
    "Add First": lambda x: [first_set.add(int(num)) for num in x],
    "Add Second": lambda x: [second_set.add(int(num)) for num in x],
    "Remove First":lambda x: [first_set.discard(int(num)) for num in x],
    "Remove Second":lambda x: [second_set.discard(int(num)) for num in x],
    "Check Subset": lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
}

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    commands[first_command + " " + second_command](data)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")