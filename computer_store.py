total_price = 0
price_without_taxes = 0
taxes = 0

while True:
    line = input()

    if line == "special" or line == "regular":
        total_price = price_without_taxes + taxes
        if total_price == 0:
            print("Invalid order!")
        else:
            if line == "special":
                total_price *= 0.9

            print("Congratulations you've just bought a new computer!")
            print(f"Price without taxes: {price_without_taxes:.2f}$")
            print(f"Taxes: {taxes:.2f}$")
            print("-----------")
            print(f"Total price: {total_price:.2f}$")
        break

    price = float(line)

    if price <= 0:
        print("Invalid price!")
        continue

    price_without_taxes += price
    taxes += price * 0.2




