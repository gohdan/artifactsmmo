character_type ="main"

with open("functions.py") as functions:
    exec(functions.read())

while True:

    # ======= FIGHTING ======

    # yellow slime (2)
    print ("=== fight yellow slime ===")
    x, y = 1, -2
    do_move(x, y)
    do_unequip("weapon")
    do_equip("copper_dagger", "weapon")
    cycle_fight(10)

    # green slime (4)
    print ("=== fight green slime ===")
    x, y = 3, -2
    do_move(x, y)
    do_unequip("weapon")
    do_equip("wooden_staff", "weapon")
    cycle_fight(10)

    # blue slime (6)
    print ("=== fight blue slime ===")
    x, y = 0, -2
    do_move(x, y)
    do_unequip("weapon")
    do_equip("wooden_staff", "weapon")
    cycle_fight(10)
    
    # red slime (7)
    # print ("=== fight red slime ===")
    # x, y = 2, -2
    # do_move(x, y)
    # do_unequip("weapon")
    # do_equip("wooden_staff", "weapon")
    # cycle_fight(10)

    # cow (8)
    # print ("=== fight cow ===")
    # x, y = 0, 2
    # do_move(x, y)
    # do_unequip("weapon")
    # do_equip("wooden_staff", "weapon")
    # cycle_fight(10)

    # ======= BANKING ======

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    do_bank_deposit("yellow_slimeball", 5)
    do_bank_deposit("green_slimeball", 5)
    do_bank_deposit("blue_slimeball", 5)
    do_bank_deposit("red_slimeball", 5)


