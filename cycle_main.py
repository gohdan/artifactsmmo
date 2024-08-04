character_type ="main"

with open("functions.py") as functions:
    exec(functions.read())

while True:

    # ======= GATHERING ======

    # 1 cycle of wood - ash_wood 40 (ash_plank 6, ash_wood 4)
    # 1 cycle of copper - copper_ore 78 (copper 13)

    # ash tree (woodcutting 1)
    print("=== gather ash tree ===")
    x, y = -1, 0
    do_move(x, y)
    cycle_gathering(40)

    # copper (mining 1)
    print("=== gather copper ore ===")
    x, y = 2, 0
    do_move(x, y)
    cycle_gathering(78)

    # gudgeon (fishing 1)
    print ("=== gather gudgeon ===")
    x, y = 4, 2
    do_move(x, y)
    cycle_gathering(10)

    # ======= CRAFTING ======

    # craft ash plank
    print("move to workshop woodcutting")
    x, y = -2, -3
    do_move(x, y)
    cycle_craft("ash_plank", 6)

    # craft copper
    print("move to workshop mining")
    x, y = 1, 5
    do_move(x, y)
    cycle_craft("copper", 13)

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
    do_unequip("weapon")
    do_equip("wooden_staff", "weapon")
    cycle_fight(10)

    # yellow slime (2)
    print ("=== fight yellow slime ===")
    x, y = 1, -2
    do_move(x, y)
    do_unequip("weapon")
    do_equip("copper_dagger", "weapon")
    cycle_fight(10)

    # green slime (4)
    print ("=== fight green slime ===")
    x, y = 3, -2
    do_move(x, y)
    do_unequip("weapon")
    do_equip("wooden_staff", "weapon")
    cycle_fight(10)

    # blue slime (6)
    print ("=== fight blue slime ===")
    x, y = 0, -2
    do_move(x, y)
    do_unequip("weapon")
    do_equip("wooden_staff", "weapon")
    cycle_fight(10)
    
    # red slime (7)
    print ("=== fight red slime ===")
    x, y = 2, -2
    do_move(x, y)
    do_unequip("weapon")
    do_equip("wooden_staff", "weapon")
    cycle_fight(10)

    # cow (8)
    #print ("=== fight cow ===")
    #x, y = 0, 2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_equip("wooden_staff", "weapon")
    #cycle_fight(5)

    # ======= BANKING ======

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    do_bank_deposit("ash_wood", 10)
    do_bank_deposit("copper_ore", 10)

    do_bank_deposit("ash_plank", 1)
    do_bank_deposit("copper", 1)

    do_bank_deposit("feather", 5)
    do_bank_deposit("egg", 5)
    do_bank_deposit("raw_chicken", 5)
    do_bank_deposit("gudgeon", 5)

    do_bank_deposit("yellow_slimeball", 10)
    do_bank_deposit("green_slimeball", 10)
    do_bank_deposit("blue_slimeball", 10)
    do_bank_deposit("red_slimeball", 10)

    do_bank_deposit("wooden_stick", 1)
    do_bank_deposit("wooden_shield", 1)
    do_bank_deposit("wooden_staff", 1)
    do_bank_deposit("copper_dagger", 1)
    do_bank_deposit("copper_helmet", 1)
    do_bank_deposit("copper_boots", 1)
    do_bank_deposit("copper_ring", 1)

