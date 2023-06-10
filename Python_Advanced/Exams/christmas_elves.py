from collections import deque

elves_energies = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

total_energy = 0
total_toys = 0
iterations = 0

while elves_energies and materials:
    elf_energy = elves_energies.popleft()

    if elf_energy < 5:
        continue

    iterations += 1
    material = materials.pop()
    current_toys = 0

    if iterations % 3 == 0:
        material *= 2
        current_toys += 1

    if elf_energy >= material:
        if iterations % 5 == 0:
            current_toys = 0
            elves_energies.append(elf_energy-material)
        else:
            elves_energies.append(elf_energy - material + 1)
            current_toys += 1

        total_energy += material
        total_toys += current_toys
    else:
        materials.append(material if iterations % 3 != 0 else material // 2)
        elves_energies.append(elf_energy * 2)

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")

if elves_energies:
    print(f"Elves left: {', '.join([str(el) for el in elves_energies])}")

if materials:
    print(f"Boxes left: {', '.join([str(el) for el in materials])}")