character_type = "main"

with open("functions.py") as functions:
    exec(functions.read())

print("=== fight flying serpent ===")

x, y = 5, 4
do_move(x, y)

do_unequip("weapon")
do_unequip("body_armor")
do_equip("greater_wooden_staff", "weapon")
do_equip("feather_coat", "body_armor")

do_fight()

