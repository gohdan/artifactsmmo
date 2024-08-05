character_type ="miner"

with open("functions.py") as functions:
    exec(functions.read())

copper_limit = 48
copper_qty = 8

iron_limit = 48
iron_qty = 8

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

    # ======= CRAFTING ======

    # craft copper, iron
    print("move to workshop mining")
    x, y = 1, 5
    do_move(x, y)
    cycle_crafting("copper", copper_qty)
    cycle_crafting("iron", iron_qty)

    # ======= FIGHTING ======

    # chicken (1)
    print ("=== fight chicken ===")
    x, y = 0, 1
    do_move(x, y)
    #do_unequip("weapon")
    #do_equip("wooden_staff", "weapon")
    cycle_fight(10)

    # ======= BANKING ======

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    # just in case
    do_bank_deposit("copper_ore", 1)
    do_bank_deposit("iron_ore", 1)

    do_bank_deposit("copper", copper_qty)
    do_bank_deposit("iron", iron_qty)

    do_bank_deposit("topaz", 1)
    do_bank_deposit("emerald", 1)
    do_bank_deposit("ruby", 1)
    do_bank_deposit("sapphire", 1)

    do_bank_deposit("feather", 5)
    do_bank_deposit("egg", 5)
    do_bank_deposit("raw_chicken", 5)
    do_bank_deposit("golden_egg", 1)

