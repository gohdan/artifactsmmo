character_type ="miner"

with open("functions.py") as functions:
    exec(functions.read())

minimal_empty_inventory = 15 # for occasional drop
copper_ore_in_copper_qty = 10
iron_ore_in_iron_qty = 10
coal_in_steel_qty = 7
iron_ore_in_steel_qty = 3

# default null values

copper_limit = 0
iron_limit = 0
coal_limit = 0
steel_limit = 0

# x6
#gold_ore_limit = 30
#gold_qty = 5

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
                "copper_ring": 1,
                "copper_armor": 1,
                "copper_legs_armor": 1
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

    # save some space for occasional drops
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory - sum(belongings.values())
    print ("inventory_limit: ", inventory_limit)

    mining_level = get_character_parameter(character, "mining_level")
    print ("mining level: ", mining_level)

    match mining_level:
        case mining_level if 1 <= mining_level < 10:
            print ("gather copper")
            copper_qty = inventory_limit // copper_ore_in_copper_qty
            copper_limit = copper_qty * copper_ore_in_copper_qty
        case mining_level if 10 <= mining_level < 20:
            print ("gather copper and iron")

            copper_limit = inventory_limit // 2
            copper_qty = copper_limit // copper_ore_in_copper_qty
            copper_limit = copper_qty * copper_ore_in_copper_qty

            iron_limit = inventory_limit - copper_limit
            iron_qty = iron_limit // iron_ore_in_iron_qty
            iron_limit = iron_qty * iron_ore_in_iron_qty

        case mining_level if 20 <= mining_level < 30:
            print ("gather copper, iron and coal")

            copper_limit = inventory_limit // 3
            copper_qty = copper_limit // copper_ore_in_copper_qty
            copper_limit = copper_qty * copper_ore_in_copper_qty

            iron_limit = inventory_limit // 3
            iron_qty = iron_limit // iron_ore_in_iron_qty
            iron_limit = iron_qty * iron_ore_in_iron_qty

            steel_limit = inventory_limit - copper_limit - iron_limit
            steel_qty = steel_limit // (coal_in_steel_qty + iron_ore_in_steel_qty)
            coal_limit = steel_qty * coal_in_steel_qty
            iron_limit = iron_limit + steel_qty * iron_ore_in_steel_qty

        case mining_level if 30 <= mining_level:
            print ("gather copper, iron, coal and gold")
            # 2do: add gold

            copper_limit = inventory_limit // 3
            copper_qty = copper_limit // copper_ore_in_copper_qty
            copper_limit = copper_qty * copper_ore_in_copper_qty

            iron_limit = inventory_limit // 3
            iron_qty = iron_limit // iron_ore_in_iron_qty
            iron_limit = iron_qty * iron_ore_in_iron_qty

            steel_limit = inventory_limit - copper_limit - iron_limit
            steel_qty = steel_limit // (coal_in_steel_qty + iron_ore_in_steel_qty)
            coal_limit = steel_qty * coal_in_steel_qty
            iron_limit = iron_limit + steel_qty * iron_ore_in_steel_qty

        case _:
            # default values
            print ("gather copper (default values)")
            copper_qty = inventory_limit // copper_ore_in_copper_qty
            copper_limit = copper_qty * copper_ore_in_copper_qty

    print ("copper_ore_in_copper_qty:", copper_ore_in_copper_qty)
    print ("copper_qty:", copper_qty)
    print ("copper_limit:", copper_limit)

    print ("iron_ore_in_iron_qty:", iron_ore_in_iron_qty)
    print ("iron_qty:", iron_qty)
    print ("iron_limit:", iron_limit)

    print ("coal_in_steel_qty:", coal_in_steel_qty)
    print ("iron_ore_in_steel_qty:", iron_ore_in_steel_qty)
    print ("coal_limit:", coal_limit)
    print ("steel_qty:", steel_qty)
 
    copper_ore_in_bank_qty = get_item_in_bank_qty('copper_ore')
    print("copper_ore_in_bank_qty:{}".format(copper_ore_in_bank_qty))
    if 0 != copper_ore_in_bank_qty:
        if copper_ore_in_bank_qty > copper_limit:
            do_bank_withdraw('copper_ore', copper_limit)
            copper_limit = 0
        else:
            do_bank_withdraw('copper_ore', copper_ore_in_bank_qty)
            copper_limit = copper_limit - copper_ore_in_bank_qty

    # ======= GATHERING ======

    ## gold ore (mining 30)
    #print("=== gather gold ore ===")
    #x, y = 10, -4
    #do_move(x, y)
    #cycle_gathering(gold_ore_limit)

    # coal (mining 20)
    if 0 != coal_limit:
        print("=== gather coal ===")
        x, y = 1, 6
        do_move(x, y)
        cycle_gathering(coal_limit)

    # iron (mining 10)
    if 0 != iron_limit:
        print("=== gather iron ore ===")
        x, y = 1, 7
        do_move(x, y)
        cycle_gathering(iron_limit)

    # copper (mining 1)
    if 0 != copper_limit:
        print("=== gather copper ore ===")
        x, y = 2, 0
        do_move(x, y)
        cycle_gathering(copper_limit)

    # ======= CRAFTING ======

    # craft copper, iron, steel, gold
    print("move to workshop mining")
    x, y = 1, 5
    do_move(x, y)

    if 0 != steel_qty:
        cycle_crafting("steel", steel_qty)
    if 0 != iron_qty:
        cycle_crafting("iron", iron_qty)
    if 0 != copper_qty:
        cycle_crafting("copper", copper_qty)

    #cycle_crafting("gold", gold_qty)

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

        case level if 6 <= level:
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

        case _:
            # default values
            # chicken (1)
            print ("=== fight chicken ===")
            do_equip_to_monster("chicken")
            x, y = 0, 1
            do_move(x, y)
            cycle_fight(10)

