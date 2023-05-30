def is_exist(key_dict, dictionary):
    return key_dict in dictionary

number_of_pieces = int(input())

pieces = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")

    pieces[piece] = {"composer": composer, "key": key}

while True:
    line = input()

    if line == "Stop":
        break

    line = line.split("|")
    command = line[0]
    piece = line[1]

    if command == "Add":
        composer = line[2]
        key = line[3]

        if is_exist(piece, pieces):
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        if is_exist(piece, pieces):
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = line[2]

        if is_exist(piece, pieces):
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, values in pieces.items():
    print(f"{piece} -> Composer: {values['composer']}, Key: {values['key']}")