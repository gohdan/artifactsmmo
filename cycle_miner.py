character_type ="miner"

with open("functions.py") as functions:
    exec(functions.read())

inventory_limit = 96
copper_qty = 16

while True:

    # ======= GATHERING ======

    # copper (mining 1)
    print("=== gather copper ore ===")
    x, y = 2, 0
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # ======= CRAFTING ======

    # craft copper
    print("move to workshop mining")
    x, y = 1, 5
    do_move(x, y)
    cycle_crafting("copper", copper_qty)

    # ======= BANKING ======

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    # just in case
    do_bank_deposit("copper_ore", 1)

    do_bank_deposit("copper", copper_qty)

