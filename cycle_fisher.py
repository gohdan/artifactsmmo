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

    do_unequip_all()

    inventory_items = get_inventory_items()

    match level:
        case level if 1 <= level < 5:
            belongings = {
                "fishing_net": 1,
                "copper_dagger": 1,
                "wooden_staff": 1,
                "copper_boots": 1,
                "copper_helmet": 1,
                "wooden_shield": 1,
                "copper_ring": 1
            }
            if "copper_dagger" not in inventory_items and "wooden_staff" not in inventory_items:
                belongings["wooden_stick"] = 1
        case level if 5 <= level:
            belongings = {
                "fishing_net": 1,
                "fire_staff": 1,
                "water_bow": 1,
                "sticky_dagger": 1,
                "sticky_sword": 1,
                "copper_boots": 1,
                "copper_helmet": 1,
                "wooden_shield": 1,
                "copper_ring": 2,
                "copper_armor": 1,
                "copper_legs_armor": 1,
                "life_amulet": 2,
                "feather_coat": 1,
                "cooked_gudgeon": 5,
                "cooked_chicken": 5,
                "cooked_beef": 5,
                "fried_eggs": 5
            }
            if "sticky_dagger" not in inventory_items:
                belongings["copper_dagger"] = 1
            if "sticky_sword" not in inventory_items:
                belongings["wooden_staff"] = 1
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

    do_bank_deposit_unnecessary(belongings)

    do_bank_withdraw_belongings(belongings)

    # ======= INVENTORY LIMITS ======

    inventory_max_items = get_character_parameter(character, "inventory_max_items")
    print ("inventory_max_items: ", inventory_max_items)

    # save some space for occasional drop
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory - sum(belongings.values())
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

    do_equip("fishing_net", "weapon")

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

    match level:
        case level if 1 <= level <  2:
            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 10)

        case level if 2 <= level < 4:
            # yellow slime (2)
            print ("=== fight yellow slime ===")
            go_fight("yellow_slime", 10)

            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 6)

        case level if 4 <= level < 5:
            # green slime (4)
            print ("=== fight green slime ===")
            go_fight("green_slime", 10)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            go_fight("yellow_slime", 5)

            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 6)

        case level if 5 <= level < 6:
            # green slime (4)
            print ("=== fight green slime ===")
            go_fight("green_slime", 10)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            go_fight("yellow_slime", 5)

            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 6)

        case level if 6 <= level < 7:
            # blue slime (6)
            print ("=== fight blue slime ===")
            go_fight("blue_slime", 10)

            # green slime (4)
            print ("=== fight green slime ===")
            go_fight("green_slime", 5)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            go_fight("yellow_slime", 3)

            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 6)

        case level if 7 <= level < 8:
            # sheep (5)
            print ("=== fight sheep ===")
            go_fight("sheep", 10)

            # red slime (7)
            print ("=== fight red slime ===")
            go_fight("red_slime", 10)

            # blue slime (6)
            print ("=== fight blue slime ===")
            go_fight("blue_slime", 5)

            # green slime (4)
            print ("=== fight green slime ===")
            go_fight("green_slime", 3)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            go_fight("yellow_slime", 3)

            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 6)

        case level if 8 <= level:
            # cow (8)
            print ("=== fight cow ===")
            go_fight("cow", 10)

            # sheep (5)
            print ("=== fight sheep ===")
            go_fight("sheep", 3)

            # red slime (7)
            print ("=== fight red slime ===")
            go_fight("red_slime", 5)

            # blue slime (6)
            print ("=== fight blue slime ===")
            go_fight("blue_slime", 5)

            # green slime (4)
            print ("=== fight green slime ===")
            go_fight("green_slime", 3)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            go_fight("yellow_slime", 3)

            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 6)

        case _:
            # default values
            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 10)

