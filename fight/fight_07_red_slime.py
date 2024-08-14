character_type = "main"

with open("functions.py") as functions:
    exec(functions.read())

print("=== fight red slime ===")

x, y = 2, -2
do_move(x, y)

do_unequip("weapon")
do_unequip("body_armor")
do_equip("sticky_sword", "weapon")
do_equip("copper_armor", "body_armor")

do_fight()

