character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft iron sword ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw iron")
do_bank_withdraw("iron", 8)

print("move to workshop weaponcrafting")
x, y = 2, 1
do_move(x, y)

do_crafting("iron_sword")

