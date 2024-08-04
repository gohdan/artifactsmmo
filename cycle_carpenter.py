character_type ="carpenter"

with open("functions.py") as functions:
    exec(functions.read())

inventory_limit = 100
ash_plank_qty = 16
ash_wood_qty = 4

while True:

    # ======= GATHERING ======

    # ash tree (woodcutting 1)
    print("=== gather ash tree ===")
    x, y = -1, 0
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # ======= CRAFTING ======

    # craft ash plank
    print("move to workshop woodcutting")
    x, y = -2, -3
    do_move(x, y)
    cycle_crafting("ash_plank", ash_plank_qty)

    # ======= BANKING ======

    # banking
    print ("=== banking ===")
    x, y = 4, 1
    do_move(x, y)

    do_bank_deposit("ash_wood", ash_wood_qty)
    do_bank_deposit("ash_plank", ash_plank_qty)

