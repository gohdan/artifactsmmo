character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft ash plank ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw ash wood")
do_bank_withdraw("ash_wood", 6)

print("move to workshop woodcutting")
x, y = -2, -3
do_move(x, y)

do_crafting("ash_plank")

