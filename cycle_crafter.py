character_type ="crafter"

with open("functions.py") as functions:
    exec(functions.read())

minimal_empty_inventory = 15 # for occasional drop

while True:
    # ======= CHARACTER INFO ======

    level = get_character_parameter(character, "level")
    print ("level: ", level)

    do_unequip_all()

    inventory_items = get_inventory_items()

    match level:
        case level if 1 <= level:
            belongings = {
                "copper_dagger": 1,
                "wooden_staff": 1,
                "copper_boots": 1,
                "copper_helmet": 1,
                "wooden_shield": 1,
                "copper_ring": 1
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

    bank_info = get_bank_info()
    print (bank_info)

    if bank_info['gold'] > bank_info['next_expansion_cost']:
        print("have enough gold to buy bank expansion, buying")
        do_bank_withdraw("gold", bank_info['next_expansion_cost'])
        buy_bank_expansion()
    else:
        print("do not have enough gold to buy bank expansion")

    inventory = get_character_parameter(character, "inventory")
    print(inventory)

    do_bank_deposit_unnecessary(belongings)

    bank_contents = get_bank_items()
    print (bank_contents)

    bank_items = {}
    for i in bank_contents:
        bank_items[i['code']] = i['quantity']

    print("bank_items:")
    print(bank_items)

    do_bank_withdraw_belongings(belongings)

    bank_contents = get_bank_items()
    print (bank_contents)

    bank_items = {}
    for i in bank_contents:
        bank_items[i['code']] = i['quantity']

    print("bank_items:")
    print(bank_items)

    # ======= INVENTORY LIMITS ======

    inventory_max_items = get_character_parameter(character, "inventory_max_items")
    print ("inventory_max_items: ", inventory_max_items)

    # save some space for monsters drop
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory - sum(belongings.values())
    print ("inventory_limit: ", inventory_limit)

    withdraw = {}

    # ======= DETERMINE: ALCHEMY ======

    alchemy_level = get_character_parameter(character, "alchemy_level")
    print ("alchemy level: ", alchemy_level)

    match alchemy_level:
        case alchemy_level if 1 <= alchemy_level:
            print ("gather sunflower")
            sunflower_limit = 10
        case _:
            # default values
            print ("gather sunflower (default values)")
            sunflower_limit = 10
    print("sunflower_limit: {}".format(sunflower_limit))

    inventory_available = inventory_limit - sunflower_limit
    print("inventory_available: {}".format(inventory_available))

    # ======= DETERMINE: WEAPONCRAFTING ======

    print("*** determine: weaponcrafting ***")

    craft_weapon = {}

    weaponcrafting_level = get_character_parameter(character, "weaponcrafting_level")
    print ("weaponcrafting level: ", weaponcrafting_level)

    match weaponcrafting_level:
        case weaponcrafting_level if 1 <= weaponcrafting_level:
            print("craft copper dagger and wooden_staff")
            target_items = ['copper_dagger', 'wooden_staff']
        case _:
            # default values
            print("craft copper dagger and wooden_staff (default values)")
            target_items = ['copper_dagger', 'wooden_staff']
    print("target_items: {}".format(target_items))

    for target_item in target_items:
        print("checking requisites of {}".format(target_item))
        match target_item:
            case target_item if "copper_dagger" == target_item:
                requisites = {'copper': 6}
            case target_item if "wooden_staff" == target_item:
                requisites = {'wooden_stick': 1, 'ash_wood': 4}
            case _:
                # default values
                print("didn't found requisites")
                requisites = {}

        print("requisites: {}".format(requisites))

        if 1 == if_requisites_available(requisites, bank_items, inventory_available):
            print("all requisites available")
            craft_weapon[target_item] = craft_weapon.get(target_item, 0) + 1
            for requisite in requisites:
                withdraw[requisite] = withdraw.get(requisite, 0) + requisites[requisite]
                bank_items[requisite] -= requisites[requisite]
                inventory_available = inventory_available - requisites[requisite]

    print("inventory_available: {}".format(inventory_available))
    print("withdraw: {}".format(withdraw))

    print("craft_weapon: {}".format(craft_weapon))

    # ======= DETERMINE: GEARCRAFTING ======

    print("*** determine: gearcrafting ***")

    craft_gear = {}

    gearcrafting_level = get_character_parameter(character, "gearcrafting_level")
    print ("gearcrafting level: ", gearcrafting_level)

    match gearcrafting_level:
        case gearcrafting_level if 1 <= gearcrafting_level:
            print("craft wooden shield, copper boots and copper helmet")
            target_items = ['wooden_shield', 'copper_boots', 'copper_helmet']
        case _:
            # default values
            print("craft wooden shield (default value)")
            target_items = ['wooden_shield']
    print("target_items: {}".format(target_items))

    for target_item in target_items:
        print("checking requisites of {}".format(target_item))
        match target_item:
            case target_item if "wooden_shield" == target_item:
                requisites = {'ash_plank': 6}
            case target_item if "copper_boots" == target_item:
                requisites = {'copper': 6}
            case target_item if "copper_helmet" == target_item:
                requisites = {'copper': 6}
            case _:
                # default values
                print("didn't found requisites")
                requisites = {}

        print("requisites: {}".format(requisites))

        if 1 == if_requisites_available(requisites, bank_items, inventory_available):
            print("all requisites available")
            craft_gear[target_item] = craft_gear.get(target_item, 0) + 1
            for requisite in requisites:
                withdraw[requisite] = withdraw.get(requisite, 0) + requisites[requisite]
                bank_items[requisite] -= requisites[requisite]
                inventory_available = inventory_available - requisites[requisite]

    print("inventory_available: {}".format(inventory_available))
    print("withdraw: {}".format(withdraw))

    print("craft_gear: {}".format(craft_gear))

    # ======= DETERMINE: JEWELRY ======

    print("*** determine: jewelry ***")

    craft_jewelry = {}

    jewelrycrafting_level = get_character_parameter(character, "jewelrycrafting_level")
    print ("jewelrycrafting level: ", jewelrycrafting_level)

    match jewelrycrafting_level:
        case jewelrycrafting_level if 1 <= jewelrycrafting_level:
            print("craft copper ring")
            target_items = ['copper_ring']
        case _:
            # default values
            print("craft copper ring (default values)")
            target_items = ['copper_ring']
    print("target_items: {}".format(target_items))

    for target_item in target_items:
        print("checking requisites of {}".format(target_item))
        match target_item:
            case target_item if "copper_ring" == target_item:
                requisites = {'copper': 6}
            case _:
                # default values
                print("didn't found requisites")
                requisites = {}

        print("requisites: {}".format(requisites))

        if 1 == if_requisites_available(requisites, bank_items, inventory_available):
            print("all requisites available")
            craft_jewelry[target_item] = craft_jewelry.get(target_item, 0) + 1
            for requisite in requisites:
                withdraw[requisite] = withdraw.get(requisite, 0) + requisites[requisite]
                bank_items[requisite] -= requisites[requisite]
                inventory_available = inventory_available - requisites[requisite]

    print("inventory_available: {}".format(inventory_available))
    print("withdraw: {}".format(withdraw))

    print("craft_jewelry: {}".format(craft_jewelry))

    # ======= DETERMINE: COOKING ======

    print("*** determine: cooking ***")

    craft_cooking = {}

    cooking_level = get_character_parameter(character, "cooking_level")
    print ("cooking level: ", cooking_level)

    # 10, shrimp: 1
    #do_crafting("cooked_shrimp")
    # 5, raw_beef: 1
    #do_crafting("cooked_beef")

    match cooking_level:
        case cooking_level if 1 <= cooking_level:
            print("cook gudgeon and chicken")
            target_items = ['cooked_chicken', 'cooked_gudgeon']
        case _:
            # default values
            print("cook gudgeon and chicken (default values)")
            target_items = ['cooked_chicken', 'cooked_gudgeon']
    print("target_items: {}".format(target_items))

    for target_item in target_items:
        print("checking requisites of {}".format(target_item))
        match target_item:
            case target_item if "cooked_gudgeon" == target_item:
                requisites = {'gudgeon': 1}
            case target_item if "cooked_chicken" == target_item:
                requisites = {'raw_chicken': 1}
            case _:
                # default values
                print("didn't found requisites")
                requisites = {}

        print("requisites: {}".format(requisites))

        if 1 == if_requisites_available(requisites, bank_items, inventory_available):
            print("all requisites available")
            craft_cooking[target_item] = craft_cooking.get(target_item, 0) + 1
            for requisite in requisites:
                withdraw[requisite] = withdraw.get(requisite, 0) + requisites[requisite]
                bank_items[requisite] -= requisites[requisite]
                inventory_available = inventory_available - requisites[requisite]

    print("inventory_available: {}".format(inventory_available))
    print("withdraw: {}".format(withdraw))

    print("craft_cooking: {}".format(craft_cooking))

    # ======= WITHDRAW ======

    print("withdraw: {}".format(withdraw))
    for i in withdraw:
        print("{}: {}".format(i, withdraw[i]))
        do_bank_withdraw(i, withdraw[i])
            
    # ======= GATHERING ======

    # sunflower (alchemy 1)
    if 0 != sunflower_limit:
        print("=== gather sunflower ===")
        x, y = 2, 2
        do_move(x, y)
        cycle_gathering(sunflower_limit)
        
    # ======= COOKING ======

    print("move to workshop cooking")
    x, y = 1, 1
    do_move(x, y)

    print("craft_cooking: {}".format(craft_cooking))

    for item in craft_cooking:
        for i in range(0, craft_cooking[item]):
            print("crafting {} {} of {}".format(item, i+1, craft_cooking[item]))
            do_crafting(item)

    # ======= WEAPONCRAFTING ======

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
    # 1 cycle of cowhide - cowhide 2
    # 1 cycle of raw beef - raw_beef 1
    # 1 cycle of shrimp - shrimp 1

    print("move to workshop weaponcrafting")
    x, y = 2, 1
    do_move(x, y)

    print("craft_weapon: {}".format(craft_weapon))

    for item in craft_weapon:
        for i in range(0, craft_weapon[item]):
            print("crafting {} {} of {}".format(item, i+1, craft_weapon[item]))
            do_crafting(item)

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
    #do_crafting("wooden_stick")
    # 1, wooden_stick: 1, ash_wood: 4
    #do_crafting("wooden_staff")
    # 1, copper: 3
    #do_crafting("copper_dagger")



    # ======= GEARCRAFTING ======

    # 5, feather: 5
    #do_crafting("feather_coat")
    # 5, copper: 5
    #do_crafting("copper_armor")
    # 5, copper: 4
    #do_crafting("copper_legs_armor")
    # 1, copper: 4
    # 5, blue_slimeball: 1, red_slimeball: 1, cowhide: 2
    #do_crafting("life_amulet")

    print("move to workshop gearcrafting")
    x, y = 3, 1
    do_move(x, y)

    print("craft_gear: {}".format(craft_gear))

    for item in craft_gear:
        for i in range(0, craft_gear[item]):
            print("crafting {} {} of {}".format(item, i+1, craft_gear[item]))
            do_crafting(item)

    # ======= JEWELRY ======

    #print("move to workshop jewelrycrafting")
    x, y = 1, 3
    do_move(x, y)

    # 1, copper: 4
    # 5, blue_slimeball: 1, red_slimeball: 1, cowhide: 2
    #do_crafting("life_amulet")

    print("craft_jewelry: {}".format(craft_jewelry))

    for item in craft_jewelry:
        for i in range(0, craft_jewelry[item]):
            print("crafting {} {} of {}".format(item, i+1, craft_jewelry[item]))
            do_crafting(item)

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

    match level:
        case level if 1 <= level <  2:
            # chicken (1)
            print ("=== fight chicken ===")
            do_equip_to_monster("chicken")
            x, y = 0, 1
            do_move(x, y)
            cycle_fight(10)

        case level if 2 <= level < 4:
            # yellow slime (2)
            print ("=== fight yellow slime ===")
            do_equip_to_monster("yellow_slime")
            x, y = 1, -2
            do_move(x, y)
            cycle_fight(10)

            # chicken (1)
            print ("=== fight chicken ===")
            do_equip_to_monster("chicken")
            x, y = 0, 1
            do_move(x, y)
            cycle_fight(5)

        case level if 4 <= level:
            # green slime (4)
            print ("=== fight green slime ===")
            do_equip_to_monster("green_slime")
            x, y = 3, -2
            do_move(x, y)
            cycle_fight(10)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            do_equip_to_monster("yellow_slime")
            x, y = 1, -2
            do_move(x, y)
            cycle_fight(5)

            # chicken (1)
            print ("=== fight chicken ===")
            do_equip_to_monster("chicken")
            x, y = 0, 1
            do_move(x, y)
            cycle_fight(3)

        case _:
            # default values
            # chicken (1)
            print ("=== fight chicken ===")
            do_equip_to_monster("chicken")
            x, y = 0, 1
            do_move(x, y)
            cycle_fight(10)

