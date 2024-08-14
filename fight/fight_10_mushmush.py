character_type = "main"

with open("functions.py") as functions:
    exec(functions.read())

print("=== fight mushmush ===")

x, y = 5, 3
do_move(x, y)

do_unequip("weapon")
do_unequip("body_armor")
do_equip("iron_dagger", "weapon")
do_equip("feather_coat", "body_armor")

do_fight()

