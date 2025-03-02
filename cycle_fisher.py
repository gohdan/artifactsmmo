character_type ="fisher"

with open("functions.py") as functions:
    exec(functions.read())

minimal_empty_inventory = 15 # for occasional drop

# default null values
gudgeon_qty = 0
shrimp_qty = 0
trout_qty = 0
bass_qty = 0

while True:
    # ======= CHARACTER INFO ======

    level = get_character_parameter(character, "level")
    print ("level: ", level)

    match level:
        case level if 1 <= level < 10:
            belongings = {
                "wooden_stick": 1
            }
        case _:
            # default values
            belongings = {
                "wooden_stick": 1
            }

    print ("belongings:", belongings)

    # ======= BANKING ======

    # banking
    print ("=== banking ===")
    x, y = 4, 1
    do_move(x, y)

    gold_qty = get_character_parameter(character, "gold")
    print("gold_qty:", gold_qty)

    if 0 != gold_qty:
        do_bank_deposit("gold", gold_qty)

    inventory = get_character_parameter(character, "inventory")
    print(inventory)

    do_bank_deposit_unnecessary(inventory, belongings)

    # ======= INVENTORY LIMITS ======

    inventory_max_items = get_character_parameter(character, "inventory_max_items")
    print ("inventory_max_items: ", inventory_max_items)

    # save some space for occasional drop
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory
    print ("inventory_limit: ", inventory_limit)

    fishing_level = get_character_parameter(character, "fishing_level")
    print ("fishing level: ", fishing_level)

    match fishing_level:
        case fishing_level if 1 <= fishing_level < 10:
            print ("gather gudgeon")
            gudgeon_qty = inventory_limit
        case fishing_level if 10 <= fishing_level < 20:
            print ("gather gudgeon and shrimp")
            #2do: add shrimp
            gudgeon_qty = inventory_limit // 2
            shrimp_qty = inventory_limit - gudgeon_qty
        case fishing_level if 20 <= fishing_level < 30:
            print ("gather gudgeon, shrimp and trout")
            gudgeon_qty = inventory_limit // 3
            shrimp_qty = inventory_limit // 3
            trout_qty = inventory_limit - gudgeon_qty - shrimp_qty
        case fishing_level if 30 <= fishing_level:
            print ("gather gudgeon, shrimp, trout and bass")
            #2do: add bass
            gudgeon_qty = inventory_limit // 3
            shrimp_qty = inventory_limit // 3
            trout_qty = inventory_limit - gudgeon_qty - shrimp_qty
        case _:
            # default values
            print ("gather gudgeon (default values)")
            gudgeon_qty = inventory_limit

    print ("gudgeon_qty:", gudgeon_qty)
    print ("shrimp_qty:", shrimp_qty)
    print ("trout_qty:", trout_qty)

    # ======= GATHERING ======

    ## bass (fishing 30)
    #print ("=== gather bass ===")
    #x, y = -3, 6
    #do_move(x, y)
    #cycle_gathering(inventory_limit)

    # trout (fishing 20)
    if 0 != trout_qty:
        print ("=== gather trout ===")
        x, y = 7, 12
        do_move(x, y)
        cycle_gathering(trout_qty)

    # shrimp (fishing 10)
    if 0 != shrimp_qty:
        print ("=== gather shrimp ===")
        x, y = 5, 2
        do_move(x, y)
        cycle_gathering(shrimp_qty)

    # gudgeon (fishing 1)
    if 0 != gudgeon_qty:
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

