character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft sticky dagger ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw copper")
do_bank_withdraw("copper", 3)
print("withdraw green slimeball")
do_bank_withdraw("green_slimeball", 2)

print("move to workshop weaponcrafting")
x, y = 2, 1
do_move(x, y)

do_crafting("sticky_dagger")

