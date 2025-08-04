character_type ="miner"

with open("functions.py") as functions:
    exec(functions.read())

minimal_empty_inventory = 15 # for occasional drop
copper_ore_in_copper_bar_qty = 10
iron_ore_in_iron_qty = 10
coal_in_steel_qty = 7
iron_ore_in_steel_qty = 3
gold_ore_in_gold_bar_qty = 10

stone_in_gem_qty = 24

# default null values

copper_bar_qty = 0

copper_limit = 0
iron_limit = 0
coal_limit = 0
steel_limit = 0
gold_limit = 0

ruby_stone_qty = 0
emerald_stone_qty = 0
sapphire_stone_qty = 0
topaz_stone_qty = 0

while True:
    # ======= CHARACTER INFO ======

    level = get_character_parameter(character, "level")
    print ("level: ", level)

    do_unequip_all()

    inventory_items = get_inventory_items()

    match level:
        case level if 1 <= level < 5:
            belongings = {
                "copper_pickaxe": 1,
                "copper_dagger": 1,
                "wooden_staff": 1,
                "copper_boots": 1,
                "copper_helmet": 1,
                "wooden_shield": 1,
                "copper_ring": 1
            }
            if "copper_dagger" not in inventory_items and "wooden_staff" not in inventory_items:
                belongings["wooden_stick"] = 1
        case level if 5 <= level < 10:
            belongings = {
                "copper_pickaxe": 1,
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

        case level if 10 <= level:
            belongings = {
                "fire_bow": 1,
                "greater_wooden_staff": 1,
                "iron_dagger": 1,
                "iron_sword": 1,

                "slime_shield": 1,

                "iron_armor": 1,
                "leather_armor": 1,
                "adventurer_vest": 1,

                "leather_hat": 1,
                "iron_helm": 1,
                "adventurer_helmet": 1,

                "leather_legs_armor": 1,
                "iron_legs_armor": 1,

                "leather_boots": 1,
                "iron_boots": 1,

                "iron_ring": 2,

                "life_amulet": 1,
                "fire_and_earth_amulet": 1,
                "air_and_water_amulet": 1,

                "small_health_potion": 10,

                "air_boost_potion": 10,
                "earth_boost_potion": 10,
                "fire_boost_potion": 10,
                "water_boost_potion": 10,

                "cooked_gudgeon": 10,
                "cooked_chicken": 10,
                "cooked_beef": 10,
                "fried_eggs": 10,
                "cheese": 10,
                "cooked_shrimp": 10
            }

            if "leather_boots" not in inventory_items and "iron_boots" not in inventory_items:
                belongings["copper_boots"] = 1
            if "leather_hat" not in inventory_items and "iron_helm" not in inventory_items and "adventurer_helmet" not in inventory_items:
                belongings["copper_helmet"] = 1

            if "slime_shield" not in inventory_items:
                belongings["wooden_shield"] = 1

            if "iron_armor" not in inventory_items:
                belongings["copper_armor"] = 1
            if "leather_armor" not in inventory_items:
                belongings["feather_coat"] = 1

            if "leather_legs_armor" not in inventory_items and "iron_legs_armor" not in inventory_items:
                belongings["copper_legs_armor"] = 1

            if "iron_ring" not in inventory_items:
                belongings["copper_ring"] = 2

            # Damage: Air
            if "iron_dagger" not in inventory_items and "sticky_dagger" not in inventory_items:
                belongings["copper_dagger"] = 1
            elif "iron_dagger" not in inventory_items:
                belongings["sticky_dagger"] = 1

            # Damage: Earth 
            if "iron_sword" not in inventory_items and "sticky_sword" not in inventory_items:
                belongings["wooden_staff"] = 1
            elif "iron_sword" not in inventory_items:
                belongings["sticky_sword"] = 1

            # Damage: Water
            if "greater_wooden_staff" not in inventory_items:
                belongings["water_bow"] = 1

            # Damage: Fire
            if "fire_bow" not in inventory_items:
                belongings["fire_staff"] = 1

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

    # ======= GEMS CRAFTING ======

    mining_level = get_character_parameter(character, "mining_level")
    print ("mining level: ", mining_level)

    if mining_level >= 20:
        gems = {'ruby', 'emerald', 'sapphire', 'topaz'}
        for gem in gems:
            print("check gem:", gem)
            stone_name = gem + "_stone"
            print("stone_name:{}".format(stone_name))
            stone_in_bank_qty = get_item_in_bank_qty(stone_name)
            print("stone_in_bank_qty:{}".format(stone_in_bank_qty))
            if stone_in_gem_qty <= stone_in_bank_qty:
                do_bank_withdraw(stone_name, stone_in_gem_qty)
                print("move to workshop mining")
                x, y = 1, 5
                do_move(x, y)
                do_crafting(gem)
                print ("=== banking ===")
                x, y = 4, 1
                do_move(x, y)
                do_bank_deposit(gem, 1)

    # ======= INVENTORY LIMITS ======

    inventory_max_items = get_character_parameter(character, "inventory_max_items")

    print ("inventory_max_items: ", inventory_max_items)

    # save some space for occasional drops
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory - sum(belongings.values())
    print ("inventory_limit: ", inventory_limit)

    iron_qty = 0;
    steel_qty = 0;

    crafter_weaponcrafting_level = get_character_parameter(characters["crafter"], "weaponcrafting_level")
    crafter_gearcrafting_level = get_character_parameter(characters["crafter"], "gearcrafting_level")
    crafter_jewelrycrafting_level = get_character_parameter(characters["crafter"], "jewelrycrafting_level")

    copper_bar_in_bank_qty = get_item_in_bank_qty("copper_bar")
    print("copper_bar_in_bank_qty:{}".format(copper_bar_in_bank_qty))

    need_copper_bars = 0
    if crafter_weaponcrafting_level < 10 or crafter_gearcrafting_level < 10 or crafter_jewelrycrafting_level < 5:
        if copper_bar_in_bank_qty <= 10:
            need_copper_bars = 1
    print("need_copper_bars: {}".format(need_copper_bars))

    match mining_level:
        case mining_level if 1 <= mining_level < 10:
            print ("gather copper")
            copper_bar_qty = inventory_limit // copper_ore_in_copper_bar_qty
            copper_limit = copper_bar_qty * copper_ore_in_copper_bar_qty

        case mining_level if 10 <= mining_level < 20:
            if 1 == need_copper_bars:
                print ("gather copper")
                copper_bar_qty = inventory_limit // copper_ore_in_copper_bar_qty
                copper_limit = copper_bar_qty * copper_ore_in_copper_bar_qty
            else:
                print ("gather copper and iron")
                copper_limit = inventory_limit // 2
                copper_bar_qty = copper_limit // copper_ore_in_copper_bar_qty
                copper_limit = copper_bar_qty * copper_ore_in_copper_bar_qty

                iron_limit = inventory_limit - copper_limit
                iron_qty = iron_limit // iron_ore_in_iron_qty
                iron_limit = iron_qty * iron_ore_in_iron_qty

        case mining_level if 20 <= mining_level < 30:
            if 1 == need_copper_bars:
                print ("gather copper")
                copper_bar_qty = inventory_limit // copper_ore_in_copper_bar_qty
                copper_limit = copper_bar_qty * copper_ore_in_copper_bar_qty
            else:
                print ("gather copper, iron and coal")

                copper_limit = inventory_limit // 3
                copper_bar_qty = copper_limit // copper_ore_in_copper_bar_qty
                copper_limit = copper_bar_qty * copper_ore_in_copper_bar_qty

                iron_limit = inventory_limit // 3
                iron_qty = iron_limit // iron_ore_in_iron_qty
                iron_limit = iron_qty * iron_ore_in_iron_qty

                steel_limit = inventory_limit - copper_limit - iron_limit
                steel_qty = steel_limit // (coal_in_steel_qty + iron_ore_in_steel_qty)
                coal_limit = steel_qty * coal_in_steel_qty
                iron_limit = iron_limit + steel_qty * iron_ore_in_steel_qty

        case mining_level if 30 <= mining_level:
            if 1 == need_copper_bars:
                print ("gather copper")
                copper_bar_qty = inventory_limit // copper_ore_in_copper_bar_qty
                copper_limit = copper_bar_qty * copper_ore_in_copper_bar_qty
            else:
                print ("gather iron, coal and gold")

                gold_limit = inventory_limit // 2
                gold_bar_qty = gold_limit // gold_ore_in_gold_bar_qty
                gold_limit = gold_bar_qty * gold_ore_in_gold_bar_qty

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
            copper_bar_qty = inventory_limit // copper_ore_in_copper_bar_qty
            copper_limit = copper_bar_qty * copper_ore_in_copper_bar_qty

    print ("copper_ore_in_copper_bar_qty:", copper_ore_in_copper_bar_qty)
    print ("copper_bar_qty:", copper_bar_qty)
    print ("copper_limit:", copper_limit)

    print ("iron_ore_in_iron_qty:", iron_ore_in_iron_qty)
    print ("iron_qty:", iron_qty)
    print ("iron_limit:", iron_limit)

    print ("coal_in_steel_qty:", coal_in_steel_qty)
    print ("iron_ore_in_steel_qty:", iron_ore_in_steel_qty)
    print ("coal_limit:", coal_limit)
    print ("steel_qty:", steel_qty)

    print ("gold_ore_in_gold_bar_qty:", gold_ore_in_gold_bar_qty)
    print ("gold_bar_qty:", gold_bar_qty)
    print ("gold_limit:", gold_limit)

    copper_ore_in_bank_qty = get_item_in_bank_qty('copper_ore')
    print("copper_ore_in_bank_qty:{}".format(copper_ore_in_bank_qty))
    if 0 != copper_ore_in_bank_qty:
        if copper_ore_in_bank_qty > copper_limit:
            do_bank_withdraw('copper_ore', copper_limit)
            copper_limit = 0
        else:
            do_bank_withdraw('copper_ore', copper_ore_in_bank_qty)
            copper_limit = copper_limit - copper_ore_in_bank_qty

    iron_ore_in_bank_qty = get_item_in_bank_qty('iron_ore')
    print("iron_ore_in_bank_qty:{}".format(iron_ore_in_bank_qty))
    if 0 != iron_ore_in_bank_qty:
        if iron_ore_in_bank_qty > iron_limit:
            do_bank_withdraw('iron_ore', iron_limit)
            iron_limit = 0
        else:
            do_bank_withdraw('iron_ore', iron_ore_in_bank_qty)
            iron_limit = iron_limit - iron_ore_in_bank_qty

    coal_in_bank_qty = get_item_in_bank_qty('coal')
    print("coal_in_bank_qty:{}".format(coal_in_bank_qty))
    if 0 != coal_in_bank_qty:
        if coal_in_bank_qty > coal_limit:
            do_bank_withdraw('coal', coal_limit)
            coal_limit = 0
        else:
            do_bank_withdraw('coal', coal_in_bank_qty)
            coal_limit = coal_limit - coal_in_bank_qty

    gold_ore_in_bank_qty = get_item_in_bank_qty('gold_ore')
    print("gold_ore_in_bank_qty:{}".format(gold_ore_in_bank_qty))
    if 0 != gold_ore_in_bank_qty:
        if gold_ore_in_bank_qty > gold_limit:
            do_bank_withdraw('gold_ore', gold_limit)
            gold_limit = 0
        else:
            do_bank_withdraw('gold_ore', gold_ore_in_bank_qty)
            gold_limit = gold_limit - gold_ore_in_bank_qty

    # ======= GATHERING ======

    do_equip("copper_pickaxe", "weapon")

    # gold ore (mining 30)
    if 0 != gold_limit:
        print("=== gather gold ===")
        x, y = 6, -3
        do_move(x, y)
        cycle_gathering(gold_limit)

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

    if 0 != gold_bar_qty:
        cycle_crafting("gold_bar", gold_bar_qty)
    if 0 != steel_qty:
        cycle_crafting("steel_bar", steel_qty)
    if 0 != iron_qty:
        cycle_crafting("iron_bar", iron_qty)
    if 0 != copper_bar_qty:
        cycle_crafting("copper_bar", copper_bar_qty)

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

        case level if 19 <= level < 20:
            # mushmush (10)
            print ("=== fight mushmush ===")
            go_fight("mushmush", 10)

            # cow (8)
            print ("=== fight cow ===")
            go_fight("cow", 5)

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

