def shopping_list(budget, **products):
    if budget < 100:
        return "You do not have enough budget."

    result = ""
    bought_products = 0

    for product, values in products.items():
        amount = values[0] * values[1]

        if budget - amount < 0:
            continue

        if bought_products >= 5:
            break

        budget -= amount
        bought_products += 1
        result += f"You bought {product} for {amount:.2f} leva.\n"

    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
