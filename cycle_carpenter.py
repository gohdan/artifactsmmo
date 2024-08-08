character_type ="carpenter"

with open("functions.py") as functions:
    exec(functions.read())

# 6 (ash_plank) + 4 (wooden_stick) + 2 (hardwood_plank)
ash_limit = 44
ash_plank_qty = 5
ash_wood_qty = 2

# 6
spruce_limit = 36
spruce_plank_qty = 6

# x4
birch_limit = 24
hardwood_plank_qty = 6


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

    # birch tree (woodcutting 20)
    print("=== gather birch tree ===")
    x, y = 3, 5
    do_move(x, y)
    cycle_gathering(birch_limit)

    # ======= CRAFTING ======

    # craft ash plank, spruce_plank
    print("move to workshop woodcutting")
    x, y = -2, -3
    do_move(x, y)
    cycle_crafting("ash_plank", ash_plank_qty)
    cycle_crafting("spruce_plank", spruce_plank_qty)
    cycle_crafting("hardwood_plank", hardwood_plank_qty)

    # ======= FIGHTING ======

    # green slime (4)
    print ("=== fight green slime ===")
    x, y = 3, -2
    do_move(x, y)
    do_unequip("weapon")
    do_unequip("body_armor")
    #do_equip("wooden_staff", "weapon")
    do_equip("sticky_sword", "weapon")
    do_equip("copper_armor", "body_armor")
    cycle_fight(10)

    # yellow slime (2)
    print ("=== fight yellow slime ===")
    x, y = 1, -2
    do_move(x, y)
    do_unequip("weapon")
    do_unequip("body_armor")
    #do_equip("copper_dagger", "weapon")
    do_equip("sticky_dagger", "weapon")
    do_equip("feather_coat", "body_armor")
    cycle_fight(10)

    # chicken (1)
    print ("=== fight chicken ===")
    x, y = 0, 1
    do_move(x, y)
    do_unequip("weapon")
    do_unequip("body_armor")
    #do_equip("wooden_staff", "weapon")
    do_equip("sticky_sword", "weapon")
    do_equip("copper_armor", "body_armor")
    cycle_fight(10)

    # ======= BANKING ======

    # banking
    print ("=== banking ===")
    x, y = 4, 1
    do_move(x, y)

    do_bank_deposit("ash_wood", ash_wood_qty)
    do_bank_deposit("ash_plank", ash_plank_qty)
    do_bank_deposit("spruce_plank", spruce_plank_qty)
    do_bank_deposit("hardwood_plank", hardwood_plank_qty)

    do_bank_deposit("feather", 5)
    do_bank_deposit("egg", 5)
    do_bank_deposit("raw_chicken", 5)
    do_bank_deposit("golden_egg", 1)

    do_bank_deposit("yellow_slimeball", 5)
    do_bank_deposit("green_slimeball", 5)

