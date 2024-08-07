character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft wooden stick ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw ash plank")
do_bank_withdraw("ash_plank", 3)

print("move to workshop weaponcrafting")
x, y = 2, 1
do_move(x, y)

do_crafting("wooden_stick")

