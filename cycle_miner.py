character_type ="miner"

with open("functions.py") as functions:
    exec(functions.read())

minimal_empty_inventory = 10 # for monsters drop
copper_ore_in_copper_qty = 6

# x6
#copper_limit = 18
#copper_qty = 3
#copper_limit = 90
#copper_qty = 15

# x6 + 4 * steel_qty
#iron_limit = 30 + 20
#iron_qty = 5

# x4
#coal_limit = 20
#steel_qty = 5

# x6
#gold_ore_limit = 30
#gold_qty = 5

while True:
    # ======= INVENTORY LIMITS ======

    print ("get character parameters")
    level = get_character_parameter(character, "level")
    mining_level = get_character_parameter(character, "mining_level")
    inventory_max_items = get_character_parameter(character, "inventory_max_items")
    print ("end: get character parameters")

    print ("level: ", level)
    print ("mining level: ", mining_level)
    print ("inventory_max_items: ", inventory_max_items)

    # save some space for monsters drop
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory
    print ("inventory_limit: ", inventory_limit)


    match mining_level:
        case mining_level if 1 <= mining_level < 10:
            print ("gather copper")
            copper_qty = inventory_limit // copper_ore_in_copper_qty
            copper_limit = copper_qty * copper_ore_in_copper_qty
        case mining_level if 10 <= mining_level < 20:
            print ("gather copper and iron")
            #2do: add iron
            copper_qty = inventory_limit // copper_ore_in_copper_qty
            copper_limit = copper_qty * copper_ore_in_copper_qty
        case mining_level if 20 <= mining_level < 30:
            print ("gather copper, iron and coal")
            #2do: add iron and coal
            copper_qty = inventory_limit // copper_ore_in_copper_qty
            copper_limit = copper_qty * copper_ore_in_copper_qty
        case mining_level if 30 <= mining_level:
            print ("gather copper, iron, coal and gold")
            #2do: add iron, coal and gold
            copper_qty = inventory_limit // copper_ore_in_copper_qty
            copper_limit = copper_qty * copper_ore_in_copper_qty
        case _:
            # default values
            print ("gather copper (default values)")
            copper_qty = inventory_limit // copper_ore_in_copper_qty
            copper_limit = copper_qty * copper_ore_in_copper_qty

    print ("copper ore in copper:", copper_ore_in_copper_qty)
    print ("copper_qty:", copper_qty)
    print ("copper_limit:", copper_limit)

    # ======= GATHERING ======

    ## gold ore (mining 30)
    #print("=== gather gold ore ===")
    #x, y = 10, -4
    #do_move(x, y)
    #cycle_gathering(gold_ore_limit)

    ## coal (mining 20)
    #print("=== gather coal ===")
    #x, y = 1, 6
    #do_move(x, y)
    #cycle_gathering(coal_limit)

    ## iron (mining 10)
    #print("=== gather iron ore ===")
    #x, y = 1, 7
    #do_move(x, y)
    #cycle_gathering(iron_limit)

    # copper (mining 1)
    print("=== gather copper ore ===")
    x, y = 2, 0
    do_move(x, y)
    cycle_gathering(copper_limit)

    # ======= CRAFTING ======

    # craft copper, iron, steel, gold
    print("move to workshop mining")
    x, y = 1, 5
    do_move(x, y)
    #cycle_crafting("gold", gold_qty)
    #cycle_crafting("steel", steel_qty)
    #cycle_crafting("iron", iron_qty)
    cycle_crafting("copper", copper_qty)

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

    # just in case
    do_bank_deposit("copper_ore", 1)
    do_bank_deposit("copper", copper_qty)
    do_bank_deposit("topaz", 1)
    do_bank_deposit("emerald", 1)

    #do_bank_deposit("iron_ore", 1)
    #do_bank_deposit("coal", 1)
    #do_bank_deposit("gold_ore", 1)

    #do_bank_deposit("iron", iron_qty)
    #do_bank_deposit("steel", steel_qty)
    #do_bank_deposit("gold", gold_qty)

    #do_bank_deposit("ruby", 1)
    #do_bank_deposit("sapphire", 1)

    do_bank_deposit("feather", 4)
    do_bank_deposit("egg", 4)
    do_bank_deposit("raw_chicken", 4)
    do_bank_deposit("golden_egg", 1)

    #do_bank_deposit("yellow_slimeball", 4)
    #do_bank_deposit("green_slimeball", 4)
    #do_bank_deposit("blue_slimeball", 4)

