character_type = "main"

with open("functions.py") as functions:
    exec(functions.read())

print("=== fight chicken ===")

x, y = 0, 1
do_move(x, y)

do_unequip("weapon")
do_unequip("body_armor")
#do_equip("wooden_staff", "weapon")
do_equip("sticky_sword", "weapon")
do_equip("copper_armor", "body_armor")

do_fight()

