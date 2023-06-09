def start_spring(**kwargs):
    objects = {}

    for key, value in sorted(kwargs.items()):
        if value not in objects:
            objects[value] = []

        objects[value].append(key)

    result = ""
    for key, values in sorted(objects.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{key}:\n"

        for value in values:
            result += f"-{value}\n"

    return result

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))