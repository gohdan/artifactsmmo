character_type ="main"

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

    do_bank_deposit_unnecessary(belongings)

    do_bank_withdraw_belongings(belongings)

    # ======= INVENTORY LIMITS ======

    inventory_max_items = get_character_parameter(character, "inventory_max_items")
    print ("inventory_max_items: ", inventory_max_items)

    # save some space for occasional drop
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory - len(belongings)
    print ("inventory_limit: ", inventory_limit)

    # ======= FIGHTING ======

    ## flying serpent (10)
    #print ("=== fight flying serpent ===")
    #x, y = 5, 4
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    #do_equip("greater_wooden_staff", "weapon")
    #do_equip("feather_coat", "body_armor")
    #cycle_fight(10)

    ## mushmush (10)
    #print ("=== fight mushmush ===")
    #x, y = 5, 3
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    #do_equip("iron_dagger", "weapon")
    #do_equip("feather_coat", "body_armor")
    #cycle_fight(10)

    # cow (8)
    #print ("=== fight cow ===")
    #x, y = 0, 2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("sticky_sword", "weapon")
    #do_equip("iron_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    #cycle_fight(10)
    
    ## red slime (7)
    #print ("=== fight red slime ===")
    #x, y = 2, -2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("sticky_sword", "weapon")
    #do_equip("iron_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    #cycle_fight(10)

    # blue slime (6)
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

        case level if 4 <= level:
            # green slime (4)
            print ("=== fight green slime ===")
            do_equip_to_monster("green_slime")
            x, y = 3, -2
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

