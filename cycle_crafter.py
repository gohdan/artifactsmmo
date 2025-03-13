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
        case level if 1 <= level < 5:
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
        case level if 5 <= level:
            belongings = {
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

    concurrents = {'sticky_sword', 'sticky_dagger', 'water_bow', 'fire_staff', 'copper_armor', 'copper_legs_armor', 'feather_coat', 'iron_sword', 'iron_dagger', 'greater_wooden_staff', 'fire_bow', 'iron_pickaxe', 'iron_axe', 'spruce_fishing_rod', 'leather_gloves', 'leather_armor', 'iron_armor', 'adventurer_vest', 'leather_hat', 'iron_helm', 'adventurer_helmet', 'leather_legs_armor', 'iron_legs_armor', 'leather_boots', 'iron_boots', 'slime_shield'}
    for concurrent in concurrents:
        if concurrent not in bank_items:
            bank_items[concurrent] = 0

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

    print("*** determine: alchemy ***")

    craft_alchemy = {}

    alchemy_level = get_character_parameter(character, "alchemy_level")
    print ("alchemy level: ", alchemy_level)

    match alchemy_level:
        case alchemy_level if 1 <= alchemy_level < 5:
            print ("gather sunflower")
            sunflower_limit = 9
        case alchemy_level if 5 <= alchemy_level:
            print ("gather sunflower if needed, craft small health potion")
            if bank_items['sunflower'] < 10:
                sunflower_limit = 3
            else:
                sunflower_limit = 0
            target_items = ['small_health_potion']
        case _:
            # default values
            print ("gather sunflower (default values)")
            sunflower_limit = 9
    print("sunflower_limit: {}".format(sunflower_limit))

    inventory_available = inventory_limit - sunflower_limit
    print("inventory_available: {}".format(inventory_available))

    print("target_items: {}".format(target_items))

    for target_item in target_items:
        print("checking requisites of {}".format(target_item))
        match target_item:
            case target_item if "small_health_potion" == target_item:
                requisites = {'sunflower': 3}
            case _:
                # default values
                print("didn't found requisites")
                requisites = {}

        print("requisites: {}".format(requisites))

        if 1 == if_requisites_available(requisites, bank_items, inventory_available):
            print("all requisites available")
            craft_alchemy[target_item] = craft_alchemy.get(target_item, 0) + 1
            for requisite in requisites:
                withdraw[requisite] = withdraw.get(requisite, 0) + requisites[requisite]
                bank_items[requisite] -= requisites[requisite]
                inventory_available = inventory_available - requisites[requisite]

    print("inventory_available: {}".format(inventory_available))
    print("withdraw: {}".format(withdraw))

    print("craft_alchemy: {}".format(craft_alchemy))

    # ======= DETERMINE: WEAPONCRAFTING ======

    print("*** determine: weaponcrafting ***")

    craft_weapon = {}
    target_items = list()

    weaponcrafting_level = get_character_parameter(character, "weaponcrafting_level")
    print ("weaponcrafting level: ", weaponcrafting_level)

    match weaponcrafting_level:
        case weaponcrafting_level if 1 <= weaponcrafting_level < 5:
            print("craft copper_dagger and wooden_staff")
            target_items = ['copper_dagger', 'wooden_staff']
        case weaponcrafting_level if 5 <= weaponcrafting_level < 10:
            print("craft fire_staff, sticky_dagger, sticky_sword, water_bow")
            if (bank_items['sticky_sword'] <= bank_items['sticky_dagger']) and (bank_items['sticky_sword'] <= bank_items['copper_armor']) and (bank_items['sticky_sword'] <= bank_items['copper_legs_armor']):
                target_items.append('sticky_sword')
            if (bank_items['sticky_dagger'] <= bank_items['sticky_sword']) and (bank_items['sticky_dagger'] <= bank_items['copper_armor']) and (bank_items['sticky_dagger'] <= bank_items['copper_legs_armor']):
                target_items.append('sticky_dagger')
            if (bank_items['fire_staff'] <= bank_items['water_bow']) and (bank_items['fire_staff'] <= bank_items['feather_coat']):
                target_items.append('fire_staff')
            if (bank_items['water_bow'] <= bank_items['fire_staff']) and (bank_items['water_bow'] <= bank_items['feather_coat']):
                target_items.append('water_bow')
        case weaponcrafting_level if 10 <= weaponcrafting_level:
            print("craft iron pickaxe, iron_axe, spruce_fishing_rod, leather_gloves, iron_sword, iron_dagger, greater_wooden_staff, fire_bow")
            target_items = ['leather_gloves']

            if (bank_items['iron_pickaxe'] <= bank_items['iron_axe']) and (bank_items['iron_pickaxe'] <= bank_items['spruce_fishing_rod']):
                target_items.append('iron_pickaxe')
            if (bank_items['iron_axe'] <= bank_items['iron_pickaxe']) and (bank_items['iron_axe'] <= bank_items['spruce_fishing_rod']):
                target_items.append('iron_axe')
            if (bank_items['spruce_fishing_rod'] <= bank_items['iron_axe']) and (bank_items['spruce_fishing_rod'] <= bank_items['iron_pickaxe']):
                target_items.append('spruce_fishing_rod')

            if (bank_items['iron_dagger'] <= bank_items['iron_sword']): 
                target_items.append('iron_dagger')
            if (bank_items['iron_sword'] <= bank_items['iron_dagger']): 
                target_items.append('iron_sword')

            if (bank_items['greater_wooden_staff'] <= bank_items['fire_bow']): 
                target_items.append('greater_wooden_staff')
            if (bank_items['fire_bow'] <= bank_items['greater_wooden_staff']): 
                target_items.append('fire_bow')

        case _:
            # default values
            print("craft copper dagger and wooden_staff (default values)")
            target_items = ['copper_dagger', 'wooden_staff']
    print("target_items: {}".format(target_items))

    for target_item in target_items:
        print("checking requisites of {}".format(target_item))
        match target_item:
            # 1 level
            case target_item if "wooden_staff" == target_item:
                requisites = {'wooden_stick': 1, 'ash_wood': 4}
            case target_item if "copper_dagger" == target_item:
                requisites = {'copper': 6}
            # 5 level
            case target_item if "sticky_sword" == target_item:
                requisites = {'yellow_slimeball': 2, 'copper': 5}
            case target_item if "sticky_dagger" == target_item:
                requisites = {'green_slimeball': 2, 'copper': 5}
            case target_item if "water_bow" == target_item:
                requisites = {'blue_slimeball': 2, 'ash_plank': 5}
            case target_item if "fire_staff" == target_item:
                requisites = {'red_slimeball': 2, 'ash_plank': 5}
            # 10 level
            case target_item if "iron_sword" == target_item:
                requisites = {'iron': 6, 'feather': 2}
            case target_item if "iron_dagger" == target_item:
                requisites = {'iron': 6, 'feather': 2}
            case target_item if "greater_wooden_staff" == target_item:
                requisites = {'spruce_plank': 6, 'blue_slimeball': 2}
            case target_item if "fire_bow" == target_item:
                requisites = {'spruce_plank': 6, 'red_slimeball': 2}
            case target_item if "leather_gloves" == target_item:
                requisites = {'ash_plank': 2, 'cowhide': 8, 'jasper_crystal': 1}
            case target_item if "iron_pickaxe" == target_item:
                requisites = {'spruce_plank': 2, 'iron': 8, 'jasper_crystal': 1}
            case target_item if "iron_axe" == target_item:
                requisites = {'spruce_plank': 2, 'iron': 8, 'jasper_crystal': 1}
            case target_item if "spruce_fishing_rod" == target_item:
                requisites = {'spruce_plank': 8, 'iron': 2, 'jasper_crystal': 1}
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
        case gearcrafting_level if 1 <= gearcrafting_level < 5:
            print("craft wooden shield, copper boots and copper helmet")
            target_items = ['wooden_shield', 'copper_boots', 'copper_helmet']
        case gearcrafting_level if 5 <= gearcrafting_level < 10:
            print("craft feather_coat, copper_armor, copper_legs_armor and satchel")
            target_items = ['satchel']
            if (bank_items['feather_coat'] <= bank_items['fire_staff']) and (bank_items['feather_coat'] <= bank_items['water_bow']):
                target_items.append('feather_coat')
            if (bank_items['copper_armor'] <= bank_items['copper_legs_armor']) and (bank_items['copper_armor'] <= bank_items['sticky_sword']) and (bank_items['copper_armor'] <= bank_items['sticky_dagger']):
                target_items.append('copper_armor')
            if (bank_items['copper_legs_armor'] <= bank_items['copper_armor']) and (bank_items['copper_legs_armor'] <= bank_items['sticky_sword']) and (bank_items['copper_legs_armor'] <= bank_items['sticky_dagger']):
                target_items.append('copper_legs_armor')
        case gearcrafting_level if 10 <= gearcrafting_level:
            print("craft leather and iron stuff")
            target_items = ['slime_shield']
            if (bank_items['leather_armor'] <= bank_items['iron_armor']) and (bank_items['leather_armor'] <= bank_items['adventurer_vest']):
                target_items.append('leather_armor')
            if (bank_items['iron_armor'] <= bank_items['leather_armor']) and (bank_items['iron_armor'] <= bank_items['adventurer_vest']):
                target_items.append('iron_armor')
            if (bank_items['adventurer_vest'] <= bank_items['leather_armor']) and (bank_items['adventurer_vest'] <= bank_items['iron_armor']):
                target_items.append('adventurer_vest')

            if (bank_items['leather_hat'] <= bank_items['iron_helm']) and (bank_items['leather_hat'] <= bank_items['adventurer_helmet']):
                target_items.append('leather_hat')
            if (bank_items['iron_helm'] <= bank_items['leather_hat']) and (bank_items['iron_helm'] <= bank_items['adventurer_helmet']):
                target_items.append('iron_helm')
            if (bank_items['adventurer_helmet'] <= bank_items['leather_hat']) and (bank_items['adventurer_helmet'] <= bank_items['iron_helm']):
                target_items.append('adventurer_helmet')

            if (bank_items['leather_boots'] <= bank_items['iron_boots']):
                target_items.append('leather_boots')
            if (bank_items['iron_boots'] <= bank_items['leather_boots']):
                target_items.append('iron_boots')
        case _:
            # default values
            print("craft wooden shield (default value)")
            target_items = ['wooden_shield']
    print("target_items: {}".format(target_items))

    for target_item in target_items:
        print("checking requisites of {}".format(target_item))
        match target_item:
            # 1 level
            case target_item if "wooden_shield" == target_item:
                requisites = {'ash_plank': 6}
            case target_item if "copper_boots" == target_item:
                requisites = {'copper': 6}
            case target_item if "copper_helmet" == target_item:
                requisites = {'copper': 6}
            # 5 level
            case target_item if "feather_coat" == target_item:
                requisites = {'feather': 5, 'ash_plank': 2}
            case target_item if "copper_armor" == target_item:
                requisites = {'copper': 5, 'feather': 2}
            case target_item if "copper_legs_armor" == target_item:
                requisites = {'copper': 5, 'feather': 2}
            case target_item if "satchel" == target_item:
                requisites = {'cowhide': 5, 'feather': 2, 'jasper_crystal': 1}
            # 10 level
            case target_item if "leather_armor" == target_item:
                requisites = {'spruce_plank': 4, 'cowhide': 4}
            case target_item if "iron_armor" == target_item:
                requisites = {'iron': 5, 'cowhide': 3}
            case target_item if "adventurer_vest" == target_item:
                requisites = {'feather': 2, 'cowhide': 6, 'spruce_plank': 4, 'yellow_slimeball': 4}
            case target_item if "leather_hat" == target_item:
                requisites = {'cowhide': 5, 'yellow_slimeball': 3}
            case target_item if "iron_helm" == target_item:
                requisites = {'iron': 5, 'feather': 3}
            case target_item if "adventurer_helmet" == target_item:
                requisites = {'feather': 4, 'cowhide': 3, 'spruce_plank': 3, 'mushroom': 4}
            case target_item if "leather_legs_armor" == target_item:
                requisites = {'spruce_plank': 5, 'cowhide': 3}
            case target_item if "iron_legs_armor" == target_item:
                requisites = {'iron': 5, 'cowhide': 3}
            case target_item if "leather_boots" == target_item:
                requisites = {'ash_plank': 4, 'cowhide': 4}
            case target_item if "iron_boots" == target_item:
                requisites = {'iron': 5, 'feather': 3}
            case target_item if "slime_shield" == target_item:
                requisites = {'spruce_plank': 5, 'red_slimeball': 3, 'yellow_slimeball': 3, 'green_slimeball': 3, 'blue_slimeball': 3}

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
        case jewelrycrafting_level if 1 <= jewelrycrafting_level < 5:
            print("craft copper ring")
            target_items = ['copper_ring']
        case jewelrycrafting_level if 5 <= jewelrycrafting_level:
            print("craft life amulet")
            target_items = ['life_amulet']
        case _:
            # default values
            print("craft copper ring (default values)")
            target_items = ['copper_ring']
    print("target_items: {}".format(target_items))

    for target_item in target_items:
        print("checking requisites of {}".format(target_item))
        match target_item:
            # 1 level
            case target_item if "copper_ring" == target_item:
                requisites = {'copper': 6}
            # 5 level
            case target_item if "life_amulet" == target_item:
                requisites = {'red_slimeball': 2, 'feather': 4}
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

    match cooking_level:
        case cooking_level if 1 <= cooking_level < 5:
            print("cook gudgeon and chicken")
            target_items = ['cooked_chicken', 'cooked_gudgeon']
        case cooking_level if 5 <= cooking_level:
            print("cook gudgeon, chicken, cooked_beef, fried_eggs")
            target_items = ['cooked_chicken', 'cooked_gudgeon', 'cooked_beef', 'fried_eggs']
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

                if "gudgeon" in bank_items:
                    if bank_items['gudgeon'] > inventory_available:
                        withdraw_qty = inventory_available
                    else:
                        withdraw_qty = bank_items['gudgeon']
                    craft_cooking['cooked_gudgeon'] = withdraw_qty
                    withdraw['gudgeon'] = withdraw_qty
                    bank_items['gudgeon'] -= withdraw_qty
                    inventory_available -= withdraw_qty

            case target_item if "cooked_chicken" == target_item:
                requisites = {'raw_chicken': 1}

                if "raw_chicken" in bank_items:
                    if bank_items['raw_chicken'] > inventory_available:
                        withdraw_qty = inventory_available
                    else:
                        withdraw_qty = bank_items['raw_chicken']
                    craft_cooking['cooked_chicken'] = withdraw_qty
                    withdraw['raw_chicken'] = withdraw_qty
                    bank_items['raw_chicken'] -= withdraw_qty
                    inventory_available -= withdraw_qty

            case target_item if "cooked_beef" == target_item:
                requisites = {'raw_beef': 1}

                if "raw_beef" in bank_items:
                    if bank_items['raw_beef'] > inventory_available:
                        withdraw_qty = inventory_available
                    else:
                        withdraw_qty = bank_items['raw_beef']
                    craft_cooking['cooked_beef'] = withdraw_qty
                    withdraw['raw_beef'] = withdraw_qty
                    bank_items['raw_beef'] -= withdraw_qty
                    inventory_available -= withdraw_qty

            case target_item if "fried_eggs" == target_item:
                requisites = {'egg': 2}

            case _:
                # default values
                print("didn't found requisites")
                requisites = {}

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
        
    # ======= ALCHEMY ======

    print("move to workshop alchemy")
    x, y = 2, 3
    do_move(x, y)

    print("craft_alchemy: {}".format(craft_alchemy))

    for item in craft_alchemy:
        for i in range(0, craft_alchemy[item]):
            print("crafting {} {} of {}".format(item, i+1, craft_alchemy[item]))
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

        case level if 4 <= level < 6:
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

        case level if 6 <= level < 7:
            # blue slime (6)
            print ("=== fight blue slime ===")
            do_equip_to_monster("blue_slime")
            x, y = 0, -2
            do_move(x, y)
            cycle_fight(10)

            # green slime (4)
            print ("=== fight green slime ===")
            do_equip_to_monster("green_slime")
            x, y = 3, -2
            do_move(x, y)
            cycle_fight(5)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            do_equip_to_monster("yellow_slime")
            x, y = 1, -2
            do_move(x, y)
            cycle_fight(3)

            # chicken (1)
            print ("=== fight chicken ===")
            do_equip_to_monster("chicken")
            x, y = 0, 1
            do_move(x, y)
            cycle_fight(3)

        case level if 7 <= level < 8:
            # red slime (7)
            print ("=== fight red slime ===")
            do_equip_to_monster("red_slime")
            x, y = 2, -2
            do_move(x, y)
            cycle_fight(10)

            # blue slime (6)
            print ("=== fight blue slime ===")
            do_equip_to_monster("blue_slime")
            x, y = 0, -2
            do_move(x, y)
            cycle_fight(5)

            # green slime (4)
            print ("=== fight green slime ===")
            do_equip_to_monster("green_slime")
            x, y = 3, -2
            do_move(x, y)
            cycle_fight(3)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            do_equip_to_monster("yellow_slime")
            x, y = 1, -2
            do_move(x, y)
            cycle_fight(3)

            # chicken (1)
            print ("=== fight chicken ===")
            do_equip_to_monster("chicken")
            x, y = 0, 1
            do_move(x, y)
            cycle_fight(3)

        case level if 8 <= level:
            # cow (8)
            print ("=== fight cow ===")
            do_equip_to_monster("cow")
            x, y = 0, 2
            do_move(x, y)
            cycle_fight(10)

            # red slime (7)
            print ("=== fight red slime ===")
            do_equip_to_monster("red_slime")
            x, y = 2, -2
            do_move(x, y)
            cycle_fight(5)

            # blue slime (6)
            print ("=== fight blue slime ===")
            do_equip_to_monster("blue_slime")
            x, y = 0, -2
            do_move(x, y)
            cycle_fight(3)

            # green slime (4)
            print ("=== fight green slime ===")
            do_equip_to_monster("green_slime")
            x, y = 3, -2
            do_move(x, y)
            cycle_fight(3)

            # yellow slime (2)
            print ("=== fight yellow slime ===")
            do_equip_to_monster("yellow_slime")
            x, y = 1, -2
            do_move(x, y)
            cycle_fight(3)

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

