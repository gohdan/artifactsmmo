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
        case level if 5 <= level < 10:
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
                "small_health_potion": 10,
                "cooked_gudgeon": 10,
                "cooked_chicken": 10,
                "cooked_beef": 10,
                "fried_eggs": 10
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

    # ======= INVENTORY LIMITS ======

    inventory_max_items = get_character_parameter(character, "inventory_max_items")
    print ("inventory_max_items: ", inventory_max_items)

    # save some space for occasional drop
    print ("minimal empty inventory:", minimal_empty_inventory)
    inventory_limit = inventory_max_items - minimal_empty_inventory - sum(belongings.values())
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

    match level:
        case level if 1 <= level <  2:
            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 10)

        case level if 2 <= level < 4:
            # yellow slime (2)
            print ("=== fight yellow slime ===")
            go_fight("yellow_slime", 10)

        case level if 4 <= level < 6:
            # green slime (4)
            print ("=== fight green slime ===")
            go_fight("green_slime", 10)

        case level if 6 <= level < 8:
            # blue slime (6)
            print ("=== fight blue slime ===")
            go_fight("blue_slime", 10)

        case level if 8 <= level < 9:
            # sheep (5)
            print ("=== fight sheep ===")
            go_fight("sheep", 10)

        case level if 9 <= level < 12:
            # red slime (7)
            print ("=== fight red slime ===")
            go_fight("red_slime", 10)

        case level if 12 <= level < 19:
            # cow (8)
            print ("=== fight cow ===")
            go_fight("cow", 10)

        case level if 19 <= level:
            # mushmush (10)
            print ("=== fight mushmush ===")
            go_fight("mushmush", 10)

        case _:
            # default values
            # chicken (1)
            print ("=== fight chicken ===")
            go_fight("chicken", 10)

