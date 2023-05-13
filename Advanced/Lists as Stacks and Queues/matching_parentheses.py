expression = input()

open_parents = []

for i in range(len(expression)):
    if expression[i] == "(":
        open_parents.append(i)

    if expression[i] == ")":
        print(expression[open_parents.pop():i + 1])
