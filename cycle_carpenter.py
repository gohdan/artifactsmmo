character_type ="carpenter"

with open("functions.py") as functions:
    exec(functions.read())

ash_limit = 52
ash_plank_qty = 8
ash_wood_qty = 4

spruce_limit = 48
spruce_plank_qty = 8

while True:

    # ======= GATHERING ======

    # ash tree (woodcutting 1)
    print("=== gather ash tree ===")
    x, y = -1, 0
    do_move(x, y)
    cycle_gathering(ash_limit)

    # spruce tree (woodcutting 10)
    print("=== gather spruce tree ===")
    x, y = 2, 6
    do_move(x, y)
    cycle_gathering(spruce_limit)

    # ======= CRAFTING ======

    # craft ash plank, spruce_plank
    print("move to workshop woodcutting")
    x, y = -2, -3
    do_move(x, y)
    cycle_crafting("ash_plank", ash_plank_qty)
    cycle_crafting("spruce_plank", spruce_plank_qty)

    # ======= FIGHTING ======

    # chicken (1)
    print ("=== fight chicken ===")
    x, y = 0, 1
    do_move(x, y)
    #do_unequip("weapon")
    #do_equip("wooden_staff", "weapon")
    cycle_fight(10)

    # ======= BANKING ======

    # banking
    print ("=== banking ===")
    x, y = 4, 1
    do_move(x, y)

    do_bank_deposit("ash_wood", ash_wood_qty)
    do_bank_deposit("ash_plank", ash_plank_qty)
    do_bank_deposit("spruce_plank", spruce_plank_qty)

    do_bank_deposit("feather", 5)
    do_bank_deposit("egg", 5)
    do_bank_deposit("raw_chicken", 5)
    do_bank_deposit("golden_egg", 1)

