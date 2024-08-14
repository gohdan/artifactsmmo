character_type = "main"

with open("functions.py") as functions:
    exec(functions.read())

print("=== fight wolf ===")

x, y = -3, 0
do_move(x, y)

do_unequip("weapon")
do_unequip("body_armor")
do_equip("iron_sword", "weapon")
do_equip("copper_armor", "body_armor")

do_fight()

