character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== cook cooked shrimp ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw shrimp")
do_bank_withdraw("shrimp", 1)

print("move to workshop cooking")
x, y = 1, 1
do_move(x, y)

do_crafting("cooked_shrimp")

