character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== cook cooked gudgeon ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw gudgeon")
do_bank_withdraw("gudgeon", 1)

print("move to workshop cooking")
x, y = 1, 1
do_move(x, y)

do_crafting("cooked_gudgeon")

