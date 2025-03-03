character_type ="carpenter"

with open("functions.py") as functions:
    exec(functions.read())

minimal_empty_inventory = 15 # for occasional drop

# ash_tree: 6 (ash_plank) + 4 (wooden_stick) + 2 (hardwood_plank)

ash_wood_in_plank = 6
minimal_ash_wood_qty = 4

spruce_in_plank = 6

# default values are null
ash_limit = 0
spruce_limit = 0
spruce_plank_qty = 0
birch_limit = 0
hardwood_plank_qty = 0

birch_in_plank = 6
ash_in_hardwood_plank = 4

while True:
    # ======= CHARACTER INFO ======

    level = get_character_parameter(character, "level")
    print ("level: ", level)

    do_unequip_all()

    inventory = get_character_parameter(character, "inventory")
    print(inventory)

    inventory_items = {}
    for item in inventory:
        inventory_items[item['code']] = item['quantity']

    print("inventory_items:{}".format(inventory_items))

    match level:
        case level if 1 <= level:
            belongings = {
                "copper_dagger": 1,
                "wooden_staff": 1
            }
            if "copper_dagger" not in inventory_items and "wooden_staff" not in inventory_items:
                belongings["wooden_stick"] = 1

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

    do_bank_deposit_unnecessary(inventory, belongings)

    do_bank_withdraw_belongings(inventory_items, belongings)

    # ======= INVENTORY LIMITS ======

    inventory_max_items = get_character_parameter(character, "inventory_max_items")
    print ("inventory_max_items: ", inventory_max_items)

    # save some space for monsters drop
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory
    print ("inventory_limit: ", inventory_limit)

    woodcutting_level = get_character_parameter(character, "woodcutting_level")
    print ("woodcutting level: ", woodcutting_level)

    match woodcutting_level:
        case woodcutting_level if 1 <= woodcutting_level <  10:
            print ("gather ash")
            ash_limit = inventory_limit
            ash_plank_qty = (ash_limit - minimal_ash_wood_qty) // ash_wood_in_plank
            ash_wood_qty = ash_limit - (ash_plank_qty * ash_wood_in_plank)
        case woodcutting_level if 11 <= woodcutting_level < 20:
            print ("gather ash and spruce")

            ash_limit = inventory_limit // 2
            ash_plank_qty = (ash_limit - minimal_ash_wood_qty) // ash_wood_in_plank
            ash_wood_qty = ash_limit - (ash_plank_qty * ash_wood_in_plank)

            spruce_limit = inventory_limit - ash_limit
            spruce_plank_qty = spruce_limit // spruce_in_plank
            spruce_limit = spruce_plank_qty * spruce_in_plank

        case woodcutting_level if 21 <= woodcutting_level < 30:
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
            ash_wood_qty = ash_limit - (ash_plank_qty * ash_wood_in_plank)

        case _:
            # default values
            print ("gather ash (non-matching woodcutting level)")
            ash_limit = inventory_limit
            ash_plank_qty = (ash_limit  - minimal_ash_wood_qty) // ash_wood_in_plank
            ash_wood_qty = ash_limit - ash_plank_qty

    print ("ash wood in ash plank:", ash_wood_in_plank)
    print ("minimal ash wood qty:", minimal_ash_wood_qty)
    print ("ash_limit:", ash_limit)
    print ("ash_plank_qty:", ash_plank_qty)
    print ("ash_wood_qty:", ash_wood_qty)

    print ("spruce in plank:", spruce_in_plank)
    print ("spruce_limit:", spruce_limit)
    print ("spruce_plank_qty:", spruce_plank_qty)

    print ("birch in plank:", birch_in_plank)
    print ("birch_limit:", birch_limit)
    print ("hardwood_plank_qty:", hardwood_plank_qty)

    # ======= GATHERING ======

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

    if 0 != birch_limit:
       cycle_crafting("hardwood_plank", hardwood_plank_qty)

    if 0 != spruce_limit:
        cycle_crafting("spruce_plank", spruce_plank_qty)

    if 0 != ash_limit:
        cycle_crafting("ash_plank", ash_plank_qty)

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

    match level:
        case level if 1 <= level <  2:
            # chicken (1)
            print ("=== fight chicken ===")
            do_equip_to_monster("chicken")
            x, y = 0, 1
            do_move(x, y)
            cycle_fight(10)
        case _:
            # default values
            # chicken (1)
            print ("=== fight chicken ===")
            do_equip_to_monster("chicken")
            x, y = 0, 1
            do_move(x, y)
            cycle_fight(10)

