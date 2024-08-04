with open("functions.py") as functions:
    exec(functions.read())

# bank
print("=== craft copper legs armor ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw copper")
do_bank_withdraw("copper_ore", 4)

print("move to workshop gearcrafting")
x, y = 3, 1
do_move(x, y)

do_crafting("copper_legs_armor")
