longest_intersection = set()

for _ in range(int(input())):
    first_range, second_range = [x.split(",") for x in input().split("-")]

    first_set = set(x for x in range(int(first_range[0]), int(first_range[1]) + 1))
    second_set = set(x for x in range(int(second_range[0]), int(second_range[1]) + 1))

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] "
      f"with length {len(longest_intersection)}")
