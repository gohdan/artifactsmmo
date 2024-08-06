character_type ="miner"

with open("functions.py") as functions:
    exec(functions.read())

# x6
copper_limit = 30
copper_qty = 5

# x6 + 4 * steel_qty
iron_limit = 30 + 20
iron_qty = 5

# x4
coal_limit = 20
steel_qty = 5

while True:

    # ======= GATHERING ======

    # copper (mining 1)
    print("=== gather copper ore ===")
    x, y = 2, 0
    do_move(x, y)
    cycle_gathering(copper_limit)

    # iron (mining 10)
    print("=== gather iron ore ===")
    x, y = 1, 7
    do_move(x, y)
    cycle_gathering(iron_limit)

    # coal (mining 20)
    print("=== gather coal ===")
    x, y = 1, 6
    do_move(x, y)
    cycle_gathering(coal_limit)

    # ======= CRAFTING ======

    # craft copper, iron
    print("move to workshop mining")
    x, y = 1, 5
    do_move(x, y)
    cycle_crafting("copper", copper_qty)
    cycle_crafting("iron", iron_qty)
    cycle_crafting("steel", steel_qty)

    # ======= FIGHTING ======

    # chicken (1)
    print ("=== fight chicken ===")
    x, y = 0, 1
    do_move(x, y)
    do_unequip("weapon")
    do_unequip("body_armor")
    #do_equip("wooden_staff", "weapon")
    do_equip("sticky_sword", "weapon")
    do_equip("copper_armor", "body_armor")
    cycle_fight(10)

    # yellow slime (2)
    print ("=== fight yellow slime ===")
    x, y = 1, -2
    do_move(x, y)
    do_unequip("weapon")
    do_unequip("body_armor")
    #do_equip("copper_dagger", "weapon")
    do_equip("sticky_dagger", "weapon")
    do_equip("feather_coat", "body_armor")
    cycle_fight(10)

    # ======= BANKING ======

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    # just in case
    do_bank_deposit("copper_ore", 1)
    do_bank_deposit("iron_ore", 1)
    do_bank_deposit("coal", 1)

    do_bank_deposit("copper", copper_qty)
    do_bank_deposit("iron", iron_qty)
    do_bank_deposit("steel", steel_qty)

    do_bank_deposit("topaz", 1)
    do_bank_deposit("emerald", 1)
    do_bank_deposit("ruby", 1)
    do_bank_deposit("sapphire", 1)

    do_bank_deposit("feather", 5)
    do_bank_deposit("egg", 5)
    do_bank_deposit("raw_chicken", 5)
    do_bank_deposit("golden_egg", 1)

    do_bank_deposit("yellow_slimeball", 5)

