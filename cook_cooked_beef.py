character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== cook cooked beef ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw raw beef")
do_bank_withdraw("raw_beef", 1)

print("move to workshop cooking")
x, y = 1, 1
do_move(x, y)

do_crafting("cooked_beef")

