character_type ="fisher"

with open("functions.py") as functions:
    exec(functions.read())

inventory_limit = 50
gudgeon_qty = 30
shrimp_qty = 30

while True:

    # ======= GATHERING ======

    # gudgeon (fishing 1)
    print ("=== gather gudgeon ===")
    x, y = 4, 2
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # shrimp (fishing 10)
    print ("=== gather shrimp ===")
    x, y = 5, 2
    do_move(x, y)
    cycle_gathering(inventory_limit)

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

    do_bank_deposit("gudgeon", gudgeon_qty)
    do_bank_deposit("shrimp", shrimp_qty)
    do_bank_deposit("golden_shrimp", 1)

    do_bank_deposit("feather", 5)
    do_bank_deposit("egg", 5)
    do_bank_deposit("raw_chicken", 5)

