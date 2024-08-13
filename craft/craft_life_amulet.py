character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft life amulet ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw blue slimeball")
do_bank_withdraw("blue_slimeball", 1)
print("withdraw red slimeball")
do_bank_withdraw("red_slimeball", 1)
print("withdraw red cowhide")
do_bank_withdraw("cowhide", 2)

print("move to workshop jewelrycrafting")
x, y = 1, 3
do_move(x, y)

do_crafting("life_amulet")

