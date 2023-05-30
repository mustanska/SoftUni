import re

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
barcode_regex = re.compile(pattern)
number_regex = re.compile(r"\d")

number_of_barcodes = int(input())

production_group = ""

for _ in range(number_of_barcodes):
    barcode = input()

    if not re.match(barcode_regex, barcode):
        print("Invalid barcode")
    else:
        numbers = re.findall(number_regex, barcode)

        if not numbers:
            production_group = "00"
        else:
            production_group = "".join(numbers)

        print(f"Product group: {production_group}")