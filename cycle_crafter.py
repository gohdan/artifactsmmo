character_type ="crafter"

with open("functions.py") as functions:
    exec(functions.read())

minimal_empty_inventory = 10 # for occasional drop

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

    inventory = get_character_parameter(character, "inventory")
    print(inventory)

    do_bank_deposit_unnecessary(inventory, belongings)

    # ======= INVENTORY LIMITS ======

    inventory_max_items = get_character_parameter(character, "inventory_max_items")
    print ("inventory_max_items: ", inventory_max_items)

    # save some space for monsters drop
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory
    print ("inventory_limit: ", inventory_limit)

    alchemy_level = get_character_parameter(character, "alchemy_level")
    print ("alchemy level: ", alchemy_level)

    match alchemy_level:
        case alchemy_level if 1 <= alchemy_level < 5:
            print ("gather sunflower")
            sunflower_limit = 10
        case _:
            # default values
            print ("gather sunflower (default values)")
            sunflower_limit = 10

    # ======= GATHERING ======

    # sunflower (alchemy 1)
    if 0 != sunflower_limit:
        print("=== gather sunflower ===")
        x, y = 2, 2
        do_move(x, y)
        cycle_gathering(sunflower_limit)

    # ======= CRAFTING ======

    # 1 full cycle of wood - ash_plank 15, ash_wood 4 (ash_wood 94)
    # 1 cycle of wood - ash_plank 6 (ash_wood 36)
    # 1 cycle of wood - spruce_plank 8
    # 1 full cycle of copper - copper 26 (copper_ore 156)
    # 1 cycle of copper - copper 14 (copper_ore 14 * 6 = 84)
    # 1 cycle of iron - iron 14
    # 1 cycle of feather - feather 5
    # 1 cycle of yellow slime ball - yellow_slimeball 2
    # 1 cycle of yellow slime ball - yellow_slimeball 0
    # 1 cycle of green slime ball - green_slimeball 2
    # 1 cycle of blue slime ball - blue_slimeball 3
    # 1 cycle of blue slime ball - blue_slimeball 1
    # 1 cycle of red slime ball - red_slimeball 3
    # 1 cycle of gudgeon - gudgeon 1
    # 1 cycle of raw chicken - raw_chicken 1
    # 1 cycle of cowhide - cowhide 2
    # 1 cycle of raw beef - raw_beef 1
    # 1 cycle of shrimp - shrimp 1

    print("move to bank")
    x, y = 4, 1
    do_move(x, y)

    #print("withdraw ash wood")
    #do_bank_withdraw("ash_wood", 4)

    #print("withdraw ash plank")
    #do_bank_withdraw("ash_plank", 9)
    do_bank_withdraw("ash_plank", 6)

    # print("withdraw spruce plank")
    #do_bank_withdraw("spruce_plank", 8)

    #print("withdraw copper")
    #do_bank_withdraw("copper", 26)
    do_bank_withdraw("copper", 4)

    #print("withdraw iron")
    #do_bank_withdraw("iron", 14)

    print("withdraw feather")
    do_bank_withdraw("feather", 5)

    #print("withdraw green slimeball")
    #do_bank_withdraw("green_slimeball", 2)

    #print("withdraw yellow slimeball")
    #do_bank_withdraw("yellow_slimeball", 2)

    #print("withdraw blue slimeball")
    #do_bank_withdraw("blue_slimeball", 3)
    #do_bank_withdraw("blue_slimeball", 1)

    #print("withdraw red slimeball")
    #do_bank_withdraw("red_slimeball", 3)

    #print("withdraw cowhide")
    #do_bank_withdraw("cowhide", 2)

    print("withdraw gudgeon")
    do_bank_withdraw("gudgeon", 1)

    print("withdraw raw chicken")
    do_bank_withdraw("raw_chicken", 1)

    #print("withdraw raw beef")
    #do_bank_withdraw("raw_beef", 1)

    #print("withdraw shrimp")
    #do_bank_withdraw("shrimp", 1)

    #print("move to workshop jewelrycrafting")
    x, y = 1, 3
    do_move(x, y)

    # 1, copper: 4
    do_crafting("copper_ring")
    # 5, blue_slimeball: 1, red_slimeball: 1, cowhide: 2
    #do_crafting("life_amulet")
    
    print("move to workshop weaponcrafting")
    x, y = 2, 1
    do_move(x, y)

    # 10, iron: 8
    #do_crafting("iron_sword")
    # 10, ash_plank: 3, spruce_plank: 4
    #do_crafting("greater_wooden_staff")
    # 10, copper: 2, iron: 6
    #do_crafting("iron_dagger")
    # 10, spruce_plank: 4, red_slimeball: 2
    #do_crafting("fire_bow")

    # 5, ash_plank: 3, red_slimeball: 2
    # do_crafting("fire_staff")
    # 5, copper: 3, green_slimeball: 2
    # do_crafting("sticky_dagger")
    # 5, copper: 4, yellow_slimeball: 2
    # do_crafting("sticky_sword")
    # 5, ash_plank: 3, blue_slimeball: 2
    # do_crafting("water_bow")

    # 1, ash_plank: 3
    do_crafting("wooden_stick")
    # 1, wooden_stick: 1, ash_wood: 4
    do_crafting("wooden_staff")
    # 1, copper: 3
    do_crafting("copper_dagger")

    print("move to workshop gearcrafting")
    x, y = 3, 1
    do_move(x, y)

    # 5, feather: 5
    do_crafting("feather_coat")
    # 5, copper: 5
    do_crafting("copper_armor")
    # 5, copper: 4
    do_crafting("copper_legs_armor")

    # 1, ash_plank: 3
    do_crafting("wooden_shield")
    # 1, copper: 3
    do_crafting("copper_helmet")
    # 1, copper: 3
    do_crafting("copper_boots")

    print("move to workshop cooking")
    x, y = 1, 1
    do_move(x, y)

    # 10, shrimp: 1
    #do_crafting("cooked_shrimp")
    # 5, raw_beef: 1
    #do_crafting("cooked_beef")
    # 1, gudgeon: 1
    do_crafting("cooked_gudgeon")
    # 1, raw_chicken: 1
    do_crafting("cooked_chicken")

    # ======= FIGHTING ======

    ## blue slime (6)
    #print ("=== fight blue slime ===")
    #x, y = 0, -2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("wooden_staff", "weapon")
    ##do_equip("sticky_sword", "weapon")
    #do_equip("iron_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    #cycle_fight(10)

    ## green slime (4)
    #print ("=== fight green slime ===")
    #x, y = 3, -2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("wooden_staff", "weapon")
    ##do_equip("sticky_sword", "weapon")
    #do_equip("iron_sword", "weapon")
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
    #do_equip("wooden_stick", "weapon")
    ##do_equip("wooden_staff", "weapon")
    ##do_equip("sticky_sword", "weapon")
    #do_equip("iron_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    cycle_fight(10)

