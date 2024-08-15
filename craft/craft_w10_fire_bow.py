character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft fire bow ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw spruce plank")
do_bank_withdraw("spruce_plank", 4)

print("withdraw red slimeball")
do_bank_withdraw("red_slimeball", 2)

print("move to workshop weaponcrafting")
x, y = 2, 1
do_move(x, y)

do_crafting("fire_bow")

