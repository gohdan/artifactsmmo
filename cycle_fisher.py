character_type ="fisher"

with open("functions.py") as functions:
    exec(functions.read())

inventory_limit = 100

while True:

    # ======= GATHERING ======

    # gudgeon (fishing 1)
    print ("=== gather gudgeon ===")
    x, y = 4, 2
    do_move(x, y)
    cycle_gathering(inventory_limit)

    # ======= BANKING ======

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    do_bank_deposit("gudgeon", inventory_limit)

