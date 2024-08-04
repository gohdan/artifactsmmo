with open("functions.py") as functions:
    exec(functions.read())

# bank
print("=== craft copper dagger ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw copper")
do_bank_withdraw("copper", 3)

print("move to workshop weaponcrafting")
x, y = 2, 1
do_move(x, y)

do_crafting("copper_dagger")
