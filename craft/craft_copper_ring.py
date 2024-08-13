character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft copper ring ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw copper")
do_bank_withdraw("copper", 4)

print("move to workshop jewelrycrafting")
x, y = 1, 3
do_move(x, y)

do_crafting("copper_ring")
