targets = [int(x) for x in input().split()]
shot_target = 0
while True:
    line = input()

    if line == "End":
        targets = [str(x) for x in targets]
        print(f"Shot targets: {shot_target} -> {' '.join(targets)}")
        break

    index = int(line)
    if index >= len(targets):
        continue

    if targets[index] != -1:
        shot_target += 1
        value = targets[index]
        for i in range(len(targets)):
            if i == index:
                targets[i] = -1
            elif targets[i] != -1:
                if targets[i] <= value:
                    targets[i] += value
                else:
                    targets[i] -= value
