character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft copper ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw copper ore")
do_bank_withdraw("copper_ore", 6)

print("move to workshop mining")
x, y = 1, 5
do_move(x, y)

do_crafting("copper")

