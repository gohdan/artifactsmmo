character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft iron dagger ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw copper")
do_bank_withdraw("copper", 2)
print("withdraw iron")
do_bank_withdraw("iron", 6)

print("move to workshop weaponcrafting")
x, y = 2, 1
do_move(x, y)

do_crafting("iron_dagger")

