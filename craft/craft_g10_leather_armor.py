character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft leather_armor ===")

print("move to workshop gearcrafting")
x, y = 3, 1
do_move(x, y)

do_crafting("leather_armor")

