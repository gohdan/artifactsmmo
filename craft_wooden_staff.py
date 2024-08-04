with open("functions.py") as functions:
    exec(functions.read())

print("=== craft wooden staff ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw wooden stick")
do_bank_withdraw("wooden_stick", 1)
print("withdraw ash wood")
do_bank_withdraw("ash_wood", 4)

print("move to workshop weaponcrafting")
x, y = 2, 1
do_move(x, y)

do_crafting("wooden_staff")

