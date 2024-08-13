character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft feather coat ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw feather")
do_bank_withdraw("feather", 5)

print("move to workshop gearcrafting")
x, y = 3, 1
do_move(x, y)

do_crafting("feather_coat")

