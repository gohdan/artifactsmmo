character_type ="crafter"

with open("functions.py") as functions:
    exec(functions.read())

while True:
    # ======= CRAFTING ======

    # 1 cycle of wood - ash_wood 40 (ash_plank 6, ash_wood 4)
    # 1 cycle of copper - copper_ore 78 (copper 13)

    print("move to bank")
    x, y = 4, 1
    do_move(x, y)

    print("withdraw ash wood")
    do_bank_withdraw("ash_wood", 4)

    print("withdraw ash plank")
    do_bank_withdraw("ash_plank", 6)

    print("withdraw copper")
    do_bank_withdraw("copper", 13)

    print("move to workshop weaponcrafting")
    x, y = 2, 1
    do_move(x, y)

    # ash_plank: 3
    do_crafting("wooden_stick")
    # wooden_stick: 1, ash_wood: 4
    do_crafting("wooden_staff")
    # copper: 3
    do_crafting("copper_dagger")

    print("move to workshop gearcrafting")
    x, y = 3, 1
    do_move(x, y)

    # ash_plank: 3
    do_crafting("wooden_shield")
    # copper: 3
    do_crafting("copper_helmet")
    # copper: 3
    do_crafting("copper_boots")

    print("move to workshop jewelrycrafting")
    x, y = 1, 3
    do_move(x, y)

    # copper: 4
    do_crafting("copper_ring")

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
    do_bank_deposit("ash_wood", 4)
    do_bank_deposit("ash_plank", 6)
    do_bank_deposit("copper", 13)

    do_bank_deposit("feather", 5)
    do_bank_deposit("egg", 5)
    do_bank_deposit("raw_chicken", 5)

    do_bank_deposit("wooden_stick", 1)
    do_bank_deposit("wooden_shield", 1)
    do_bank_deposit("wooden_staff", 1)
    do_bank_deposit("copper_dagger", 1)
    do_bank_deposit("copper_helmet", 1)
    do_bank_deposit("copper_boots", 1)
    do_bank_deposit("copper_ring", 1)

