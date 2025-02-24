character_type ="fisher"

with open("functions.py") as functions:
    exec(functions.read())

minimal_empty_inventory = 10 # for monsters drop

#inventory_limit = 60
#inventory_limit = 90

#gudgeon_qty = 25
gudgeon_qty = 60
#shrimp_qty = 25
#trout_qty = 25
#bass_qty = 25

while True:
    # ======= INVENTORY LIMITS ======

    print ("get character parameters")
    level = get_character_parameter(character, "level")
    fishing_level = get_character_parameter(character, "fishing_level")
    inventory_max_items = get_character_parameter(character, "inventory_max_items")
    print ("end: get character parameters")

    print ("level: ", level)
    print ("fishing level: ", fishing_level)
    print ("inventory_max_items: ", inventory_max_items)

    # save some space for monsters drop
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory
    print ("inventory_limit: ", inventory_limit)


    match fishing_level:
        case fishing_level if 1 <= fishing_level < 10:
            print ("gather gudgeon")
            gudgeon_qty = inventory_limit
        case fishing_level if 10 <= fishing_level < 20:
            print ("gather gudgeon and shrimp")
            #2do: add shrimp
            gudgeon_qty = inventory_limit
        case fishing_level if 20 <= fishing_level < 30:
            print ("gather gudgeon, shrimp and trout")
            #2do: add shrimp and trout
            gudgeon_qty = inventory_limit
        case fishing_level if 30 <= fishing_level:
            print ("gather gudgeon, shrimp, trout and bass")
            #2do: add shrimp, trout and bass
            gudgeon_qty = inventory_limit
        case _:
            # default values
            print ("gather gudgeon (default values)")
            gudgeon_qty = inventory_limit

    print ("gudgeon_qty:", gudgeon_qty)

    # ======= GATHERING ======

    ## bass (fishing 30)
    #print ("=== gather bass ===")
    #x, y = -3, 6
    #do_move(x, y)
    #cycle_gathering(inventory_limit)

    ## trout (fishing 20)
    #print ("=== gather trout ===")
    #x, y = -2, 6
    #do_move(x, y)
    #cycle_gathering(inventory_limit)

    ## shrimp (fishing 10)
    #print ("=== gather shrimp ===")
    #x, y = 5, 2
    #do_move(x, y)
    #cycle_gathering(inventory_limit)

    # gudgeon (fishing 1)
    print ("=== gather gudgeon ===")
    x, y = 4, 2
    do_move(x, y)
    cycle_gathering(gudgeon_qty)

    # ======= FIGHTING ======

    ## blue slime (6)
    #print ("=== fight blue slime ===")
    #x, y = 0, -2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("wooden_staff", "weapon")
    #do_equip("sticky_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    #cycle_fight(10)

    ## green slime (4)
    #print ("=== fight green slime ===")
    #x, y = 3, -2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("wooden_staff", "weapon")
    #do_equip("sticky_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    #cycle_fight(10)

    ## yellow slime (2)
    #print ("=== fight yellow slime ===")
    #x, y = 1, -2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("copper_dagger", "weapon")
    #do_equip("sticky_dagger", "weapon")
    #do_equip("feather_coat", "body_armor")
    #cycle_fight(10)

    # chicken (1)
    print ("=== fight chicken ===")
    x, y = 0, 1
    do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("wooden_staff", "weapon")
    #do_equip("sticky_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    cycle_fight(10)


    # ======= BANKING ======

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    do_bank_deposit("gudgeon", gudgeon_qty)
    #do_bank_deposit("shrimp", shrimp_qty)
    #do_bank_deposit("golden_shrimp", 1)
    #do_bank_deposit("trout", trout_qty)
    #do_bank_deposit("bass", bass_qty)

    do_bank_deposit("algae", 1)
    do_bank_deposit("feather", 4)
    do_bank_deposit("egg", 4)
    do_bank_deposit("raw_chicken", 4)
    do_bank_deposit("golden_egg", 1)

    #do_bank_deposit("yellow_slimeball", 4)
    #do_bank_deposit("green_slimeball", 4)
    #do_bank_deposit("blue_slimeball", 4)

