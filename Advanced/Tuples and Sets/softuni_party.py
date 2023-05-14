reservation_codes = set()

for _ in range(int(input())):
    code = input()

    if len(code) == 8:
        reservation_codes.add(code)

while True:
    coming_code = input()

    if coming_code == "END":
        print(len(reservation_codes))
        print(*sorted(reservation_codes), sep="\n")
        break

    if coming_code in reservation_codes:
        reservation_codes.remove(coming_code)
