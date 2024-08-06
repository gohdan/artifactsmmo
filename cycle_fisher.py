character_type ="fisher"

with open("functions.py") as functions:
    exec(functions.read())

inventory_limit = 60
gudgeon_qty = 30
shrimp_qty = 30
trout_qty = 30

while True:

    # ======= GATHERING ======

    # gudgeon (fishing 1)
    print ("=== gather gudgeon ===")
    x, y = 4, 2
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # shrimp (fishing 10)
    print ("=== gather shrimp ===")
    x, y = 5, 2
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # trout (fishing 20)
    print ("=== gather trout ===")
    x, y = -2, 7
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # ======= FIGHTING ======

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

    # ======= BANKING ======

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    do_bank_deposit("gudgeon", gudgeon_qty)
    do_bank_deposit("shrimp", shrimp_qty)
    do_bank_deposit("golden_shrimp", 1)
    do_bank_deposit("trout", trout_qty)

    do_bank_deposit("feather", 5)
    do_bank_deposit("egg", 5)
    do_bank_deposit("raw_chicken", 5)
    do_bank_deposit("golden_egg", 1)

    do_bank_deposit("yellow_slimeball", 5)

