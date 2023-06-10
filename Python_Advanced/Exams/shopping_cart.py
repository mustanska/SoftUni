def shopping_cart(*args):
    products_list = {"Soup": [], "Pizza": [], "Dessert": [],}

    for arg in args:
        if arg == "Stop":
            break

        meal_type, product = arg

        if product not in products_list[meal_type] and len(products_list[meal_type]) < limit_of_products[meal_type]:
            products_list[meal_type].append(product)

    result = ""
    if all([values == [] for values in products_list.values()]):
        result = "No products in the cart!"
    else:
        for meal_type, products in sorted(products_list.items(), key=lambda x: (-len(x[1]), x[0])):
            result += f"{meal_type}:\n"
            for product in sorted(products):
                result += f" - {product}\n"

    return result


limit_of_products = {
    "Soup": 3,
    "Pizza": 4,
    "Dessert": 2,
}

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))