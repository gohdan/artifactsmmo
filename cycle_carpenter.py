character_type ="carpenter"

with open("functions.py") as functions:
    exec(functions.read())

minimal_empty_inventory = 15 # for occasional drop

# ash_tree: 6 (ash_plank) + 4 (wooden_stick) + 2 (hardwood_plank)

minimal_ash_qty = 4

ash_wood_in_plank = 6
spruce_in_plank = 10
birch_in_plank = 6
ash_in_hardwood_plank = 4
dead_wood_in_plank = 10

# default values are null
ash_limit = 0
ash_plank_qty = 0
spruce_limit = 0
spruce_plank_qty = 0
birch_limit = 0
hardwood_plank_qty = 0
dead_wood_limit = 0
dead_wood_plank_qty = 0

while True:
    # ======= CHARACTER INFO ======

    level = get_character_parameter(character, "level")
    print ("level: ", level)

    do_unequip_all()

    inventory_items = get_inventory_items()

    match level:
        case level if 1 <= level < 5:
            belongings = {
                "copper_axe": 1,
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
                "copper_axe": 1,
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

    # save some space for monsters drop
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory - sum(belongings.values())
    print ("inventory_limit: ", inventory_limit)

    woodcutting_level = get_character_parameter(character, "woodcutting_level")
    print ("woodcutting level: ", woodcutting_level)

    minimal_ash_wood_qty = minimal_ash_qty
    print("minimal_ash_wood_qty: {}".format(minimal_ash_wood_qty))

    match woodcutting_level:
        case woodcutting_level if 1 <= woodcutting_level <  10:
            print ("gather ash")
            ash_limit = inventory_limit
            ash_plank_qty = (ash_limit - minimal_ash_wood_qty) // ash_wood_in_plank
        case woodcutting_level if 10 <= woodcutting_level < 20:
            print ("gather ash and spruce")

            ash_limit = inventory_limit // 2
            ash_plank_qty = (ash_limit - minimal_ash_wood_qty) // ash_wood_in_plank

            spruce_limit = inventory_limit - ash_limit
            spruce_plank_qty = spruce_limit // spruce_in_plank
            spruce_limit = spruce_plank_qty * spruce_in_plank

        case woodcutting_level if 20 <= woodcutting_level < 30:
            print ("gather ash, spruce and birch")

            birch_limit = inventory_limit // 3
            hardwood_plank_qty = birch_limit // birch_in_plank
            birch_limit = hardwood_plank_qty * birch_in_plank

            spruce_limit = inventory_limit // 3
            spruce_plank_qty = spruce_limit // spruce_in_plank
            spruce_limit = spruce_plank_qty * spruce_in_plank

            minimal_ash_wood_qty = minimal_ash_wood_qty + hardwood_plank_qty * ash_in_hardwood_plank

            ash_limit = inventory_limit - birch_limit - spruce_limit
            ash_plank_qty = (ash_limit - minimal_ash_wood_qty) // ash_wood_in_plank

        case woodcutting_level if 30 <= woodcutting_level:
            print ("gather spruce, birch and dead tree")

            dead_wood_limit = inventory_limit // 2
            dead_wood_plank_qty = dead_wood_limit // dead_wood_in_plank
            dead_wood_limit = dead_wood_plank_qty * dead_wood_in_plank

            birch_limit = inventory_limit // 3
            hardwood_plank_qty = birch_limit // birch_in_plank
            birch_limit = hardwood_plank_qty * birch_in_plank

            spruce_limit = inventory_limit - dead_wood_limit - birch_limit
            if (spruce_limit <= spruce_in_plank):
                spruce_limit = spruce_in_plank
                spruce_plank_qty = 1
            else:
                spruce_plank_qty = spruce_limit // spruce_in_plank
                spruce_limit = spruce_plank_qty * spruce_in_plank

        case _:
            # default values
            print ("gather ash (non-matching woodcutting level)")
            ash_limit = inventory_limit
            ash_plank_qty = (ash_limit  - minimal_ash_wood_qty) // ash_wood_in_plank

    print("dead wood in plank:{}".format(dead_wood_in_plank))
    print("dead wood limit:{}".format(dead_wood_limit))
    print("dead wood plank qty:{}".format(dead_wood_plank_qty))

    print("ash_in_hardwood_plank:{}".format(ash_in_hardwood_plank))
    print("birch in hardwood plank:{}".format(birch_in_plank))
    print("birch_limit:{}".format(birch_limit))
    print("hardwood_plank_qty:{}".format(hardwood_plank_qty))

    print("spruce in plank:{}".format(spruce_in_plank))
    print("spruce_limit:{}".format(spruce_limit))
    print("spruce_plank_qty:{}".format(spruce_plank_qty))

    print("ash wood in ash plank:{}".format(ash_wood_in_plank))
    print("minimal ash wood qty:{}".format(minimal_ash_wood_qty))
    print("ash_limit:{}".format(ash_limit))
    print("ash_plank_qty:{}".format(ash_plank_qty))

    birch_wood_in_bank_qty = get_item_in_bank_qty('birch_wood')
    print("birch_wood_in_bank_qty:{}".format(birch_wood_in_bank_qty))
    if birch_wood_in_bank_qty > birch_limit:
        do_bank_withdraw('birch_wood', birch_limit)
        birch_limit = 0
    else:
        do_bank_withdraw('birch_wood', birch_wood_in_bank_qty)
        birch_limit = birch_limit - birch_wood_in_bank_qty

    dead_wood_in_bank_qty = get_item_in_bank_qty('dead_wood')
    print("dead_wood_in_bank_qty:{}".format(dead_wood_in_bank_qty))
    if dead_wood_in_bank_qty > dead_wood_limit:
        do_bank_withdraw('dead_wood', dead_wood_limit)
        dead_wood_limit = 0
    else:
        do_bank_withdraw('dead_wood', dead_wood_in_bank_qty)
        dead_wood_limit = dead_wood_limit - dead_wood_in_bank_qty

    # ======= GATHERING ======

    do_equip("copper_axe", "weapon")

    # dead tree (woodcutting 30)
    if 0 != dead_wood_limit:
        print("=== gather dead tree ===")
        x, y = 9, 6
        do_move(x, y)
        cycle_gathering(dead_wood_limit)

    # birch tree (woodcutting 20)
    if 0 != birch_limit:
        print("=== gather birch tree ===")
        x, y = 3, 5
        do_move(x, y)
        cycle_gathering(birch_limit)

    # spruce tree (woodcutting 10)
    if 0 != spruce_limit:
        print("=== gather spruce tree ===")
        x, y = 2, 6
        do_move(x, y)
        cycle_gathering(spruce_limit)

    # ash tree (woodcutting 1)
    if 0 != ash_limit:
        print("=== gather ash tree ===")
        x, y = -1, 0
        do_move(x, y)
        cycle_gathering(ash_limit)

    # ======= CRAFTING ======

    # craft ash plank, spruce_plank, hardwood plank
    print("move to workshop woodcutting")
    x, y = -2, -3
    do_move(x, y)

    print("dead_wood in plank:{}".format(dead_wood_in_plank))
    print("dead_wood_plank_qty:{}".format(dead_wood_plank_qty))

    print("ash_in_hardwood_plank:{}".format(ash_in_hardwood_plank))
    print("birch in hardwood plank:{}".format(birch_in_plank))
    print("hardwood_plank_qty:{}".format(hardwood_plank_qty))

    print("spruce in plank:{}".format(spruce_in_plank))
    print("spruce_plank_qty:{}".format(spruce_plank_qty))

    print("ash wood in ash plank:{}".format(ash_wood_in_plank))
    print("ash_plank_qty:{}".format(ash_plank_qty))

    inventory_items = get_inventory_items()

    if 0 != dead_wood_plank_qty:
       cycle_crafting("dead_wood_plank", dead_wood_plank_qty)

    inventory_items = get_inventory_items()

    if 0 != hardwood_plank_qty:
       cycle_crafting("hardwood_plank", hardwood_plank_qty)

    inventory_items = get_inventory_items()

    if 0 != spruce_plank_qty:
        cycle_crafting("spruce_plank", spruce_plank_qty)

    inventory_items = get_inventory_items()

    if 0 != ash_plank_qty:
        cycle_crafting("ash_plank", ash_plank_qty)

    inventory_items = get_inventory_items()

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
            go_fight("yellow_slime", 6)

            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 6)

        case level if 5 <= level < 6:
            # green slime (4)
            print ("=== fight green slime ===")
            go_fight("green_slime", 10)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            go_fight("yellow_slime", 6)

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
            go_fight("yellow_slime", 4)

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
            go_fight("blue_slime", 8)

            # green slime (4)
            print ("=== fight green slime ===")
            go_fight("green_slime", 3)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            go_fight("yellow_slime", 4)

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
            go_fight("blue_slime", 8)

            # green slime (4)
            print ("=== fight green slime ===")
            go_fight("green_slime", 3)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            go_fight("yellow_slime", 4)

            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 6)

        case _:
            # default values
            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 10)

