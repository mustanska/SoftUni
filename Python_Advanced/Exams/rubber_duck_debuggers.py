from collections import deque

times = deque([int(x) for x in input().split()])
tasks_numbers = deque([int(x) for x in input().split()])

ducky_types_ranges = {
    "Darth Vader Ducky": lambda x: 0 <= x <= 60,
    "Thor Ducky": lambda x: 61 <= x <= 120,
    "Big Blue Rubber Ducky": lambda x: 121 <= x <= 180,
    "Small Yellow Rubber Ducky": lambda x: 181 <= x <= 240,
}

ducky_types_counts = {
 "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while times and tasks_numbers:
    time = times.popleft()
    tasks_number = tasks_numbers[-1]

    value = time * tasks_number

    for name, func in ducky_types_ranges.items():
        if func(value):
            tasks_numbers.pop()
            ducky_types_counts[name] += 1
            break
    else:
        tasks_numbers[-1] -= 2
        times.append(time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f"{name}: {count}") for name, count in ducky_types_counts.items()]
