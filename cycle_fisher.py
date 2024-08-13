character_type ="fisher"

with open("functions.py") as functions:
    exec(functions.read())

inventory_limit = 60
gudgeon_qty = 20
shrimp_qty = 20
trout_qty = 20
bass_qty = 20

while True:

    # ======= GATHERING ======

    # bass (fishing 30)
    print ("=== gather bass ===")
    x, y = -3, 6
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # trout (fishing 20)
    print ("=== gather trout ===")
    x, y = -2, 6
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # shrimp (fishing 10)
    print ("=== gather shrimp ===")
    x, y = 5, 2
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # gudgeon (fishing 1)
    print ("=== gather gudgeon ===")
    x, y = 4, 2
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # ======= FIGHTING ======

    # blue slime (6)
    print ("=== fight blue slime ===")
    x, y = 0, -2
    do_move(x, y)
    do_unequip("weapon")
    do_unequip("body_armor")
    #do_equip("wooden_staff", "weapon")
    do_equip("sticky_sword", "weapon")
    do_equip("copper_armor", "body_armor")
    cycle_fight(10)

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

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    do_bank_deposit("gudgeon", gudgeon_qty)
    do_bank_deposit("shrimp", shrimp_qty)
    do_bank_deposit("golden_shrimp", 1)
    do_bank_deposit("trout", trout_qty)
    do_bank_deposit("bass", bass_qty)

    do_bank_deposit("feather", 4)
    do_bank_deposit("egg", 4)
    do_bank_deposit("raw_chicken", 4)
    do_bank_deposit("golden_egg", 1)

    do_bank_deposit("yellow_slimeball", 4)
    do_bank_deposit("green_slimeball", 4)
    do_bank_deposit("blue_slimeball", 4)

