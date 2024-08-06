character_type ="crafter"

with open("functions.py") as functions:
    exec(functions.read())

while True:
    # ======= CRAFTING ======

    # 1 full cycle of wood - ash_plank 9, ash_wood 4 (ash_wood 58)
    # 1 cycle of wood - ash_plank 6 (ash_wood 36)
    # 1 full cycle of copper - copper 26 (copper_ore 156)
    # 1 cycle of copper - copper 23 (copper_ore 138)
    # 1 cycle of feather - feather 5
    # 1 cycle of green slime ball - green_slimeball 2
    # 1 cycle of yellow slime ball - yellow_slimeball 2
    # 1 cycle of blue slime ball - blue_slimeball 2
    # 1 cycle of gudgeon - gudgeon 1
    # 1 cycle of raw chicken - raw_chicken 1

    print("move to bank")
    x, y = 4, 1
    do_move(x, y)

    # print("withdraw ash wood")
    # do_bank_withdraw("ash_wood", 4)

    # print("withdraw ash plank")
    # do_bank_withdraw("ash_plank", 9)
    do_bank_withdraw("ash_plank", 6)

    print("withdraw copper")
    #do_bank_withdraw("copper", 26)
    do_bank_withdraw("copper", 23)

    print("withdraw feather")
    do_bank_withdraw("feather", 5)

    print("withdraw green slimeball")
    do_bank_withdraw("green_slimeball", 2)

    print("withdraw yellow slimeball")
    do_bank_withdraw("yellow_slimeball", 2)

    print("withdraw blue slimeball")
    do_bank_withdraw("blue_slimeball", 2)

    print("withdraw gudgeon")
    do_bank_withdraw("gudgeon", 1)

    print("withdraw raw chicken")
    do_bank_withdraw("raw_chicken", 1)

    print("move to workshop weaponcrafting")
    x, y = 2, 1
    do_move(x, y)

    # 5, copper: 3, green_slimeball: 2
    do_crafting("sticky_dagger")
    # 5, copper: 4, yellow_slimeball: 2
    do_crafting("sticky_sword")
    # 5, ash_plank: 3, blue_slimeball: 2
    do_crafting("water_bow")

    # 1, ash_plank: 3
    # do_crafting("wooden_stick")
    # 1, wooden_stick: 1, ash_wood: 4
    # do_crafting("wooden_staff")
    # 1, copper: 3
    # do_crafting("copper_dagger")

    print("move to workshop gearcrafting")
    x, y = 3, 1
    do_move(x, y)

    # 5, feather: 5
    do_crafting("feather_coat")
    # 5, copper: 5
    do_crafting("copper_armor")
    # 5, copper: 4
    do_crafting("copper_legs_armor")

    # 1, ash_plank: 3
    do_crafting("wooden_shield")
    # 1, copper: 3
    do_crafting("copper_helmet")
    # 1, copper: 3
    do_crafting("copper_boots")

    print("move to workshop jewelrycrafting")
    x, y = 1, 3
    do_move(x, y)

    # 1, copper: 4
    do_crafting("copper_ring")

    print("move to workshop cooking")
    x, y = 1, 1
    do_move(x, y)

    # 1, gudgeon: 1
    do_crafting("cooked_gudgeon")
    # 1, raw_chicken: 1
    do_crafting("cooked_chicken")

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
    do_bank_deposit("copper", 23)

    do_bank_deposit("feather", 5)
    do_bank_deposit("egg", 5)
    do_bank_deposit("raw_chicken", 5)
    do_bank_deposit("golden_egg", 1)
    do_bank_deposit("gudgeon", 5)

    do_bank_deposit("green_slimeball", 2)
    do_bank_deposit("yellow_slimeball", 2)
    do_bank_deposit("blue_slimeball", 2)

    do_bank_deposit("wooden_stick", 1)
    do_bank_deposit("wooden_shield", 1)
    do_bank_deposit("wooden_staff", 1)
    do_bank_deposit("copper_dagger", 1)
    do_bank_deposit("copper_helmet", 1)
    do_bank_deposit("copper_boots", 1)
    do_bank_deposit("copper_ring", 1)

    do_bank_deposit("feather_coat", 1)
    do_bank_deposit("copper_armor", 1)
    do_bank_deposit("copper_legs_armor", 1)
    do_bank_deposit("sticky_dagger", 1)
    do_bank_deposit("sticky_sword", 1)
    do_bank_deposit("water_bow", 1)

    do_bank_deposit("cooked_gudgeon", 1)
    do_bank_deposit("cooked_chicken", 1)

