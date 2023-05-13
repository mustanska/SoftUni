people = int(input())
wagons = [int(x) for x in input().split()]
MAX_PEOPLE = 4
is_empty = False

for i, n in enumerate(wagons):
    if n < MAX_PEOPLE:
        add_people = min(MAX_PEOPLE - n, people)
        people -= add_people
        wagons[i] = n + add_people

    if wagons[i] < MAX_PEOPLE:
        is_empty = True

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

if is_empty:
    print("The lift has empty spots!")


print(*wagons, sep=" ")
