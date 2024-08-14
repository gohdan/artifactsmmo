character_type ="crafter"

with open("functions.py") as functions:
    exec(functions.read())

while True:
    # ======= CRAFTING ======

    # 1 full cycle of wood - ash_plank 15, ash_wood 4 (ash_wood 94)
    # 1 cycle of wood - ash_plank 9 (ash_wood 54)
    # 1 cycle of wood - spruce_plank 4
    # 1 full cycle of copper - copper 26 (copper_ore 156)
    # 1 cycle of copper - copper 18 (copper_ore 18 * 6 = 150)
    # 1 cycle of feather - feather 5
    # 1 cycle of yellow slime ball - yellow_slimeball 2
    # 1 cycle of green slime ball - green_slimeball 2
    # 1 cycle of blue slime ball - blue_slimeball 3
    # 1 cycle of blue slime ball - blue_slimeball 1
    # 1 cycle of red slime ball - red_slimeball 3
    # 1 cycle of gudgeon - gudgeon 1
    # 1 cycle of raw chicken - raw_chicken 1
    # 1 cycle of cowhide - cowhide 2
    # 1 cycle of raw beef - raw_beef 1
    # 1 cycle of shrimp - shrimp 1

    print("move to bank")
    x, y = 4, 1
    do_move(x, y)

    # print("withdraw ash wood")
    # do_bank_withdraw("ash_wood", 4)

    # print("withdraw ash plank")
    # do_bank_withdraw("ash_plank", 9)
    do_bank_withdraw("ash_plank", 12)

    # print("withdraw spruce plank")
    do_bank_withdraw("spruce_plank", 4)

    print("withdraw copper")
    #do_bank_withdraw("copper", 26)
    do_bank_withdraw("copper", 18)

    print("withdraw feather")
    do_bank_withdraw("feather", 5)

    print("withdraw green slimeball")
    do_bank_withdraw("green_slimeball", 2)

    print("withdraw yellow slimeball")
    do_bank_withdraw("yellow_slimeball", 2)

    print("withdraw blue slimeball")
    #do_bank_withdraw("blue_slimeball", 3)
    do_bank_withdraw("blue_slimeball", 1)

    print("withdraw red slimeball")
    do_bank_withdraw("red_slimeball", 3)

    print("withdraw cowhide")
    do_bank_withdraw("cowhide", 2)

    print("withdraw gudgeon")
    do_bank_withdraw("gudgeon", 1)

    print("withdraw raw chicken")
    do_bank_withdraw("raw_chicken", 1)

    print("withdraw raw beef")
    do_bank_withdraw("raw_beef", 1)

    print("withdraw shrimp")
    do_bank_withdraw("shrimp", 1)

    print("move to workshop jewelrycrafting")
    x, y = 1, 3
    do_move(x, y)

    # 1, copper: 4
    #do_crafting("copper_ring")
    # 5, blue_slimeball: 1, red_slimeball: 1, cowhide: 2
    do_crafting("life_amulet")
    
    print("move to workshop weaponcrafting")
    x, y = 2, 1
    do_move(x, y)

    # 10, ash_plank: 3, spruce_plank: 4
    do_crafting("greater_wooden_staff")
    # 10, copper: 2, iron: 6
    do_crafting("iron_dagger")

    # 5, ash_plank: 3, red_slimeball: 2
    do_crafting("fire_staff")
    # 5, copper: 3, green_slimeball: 2
    # do_crafting("sticky_dagger")
    # 5, copper: 4, yellow_slimeball: 2
    do_crafting("sticky_sword")
    # 5, ash_plank: 3, blue_slimeball: 2
    # do_crafting("water_bow")

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

    print("move to workshop cooking")
    x, y = 1, 1
    do_move(x, y)

    # 10, shrimp: 1
    do_crafting("cooked_shrimp")
    # 5, raw_beef: 1
    do_crafting("cooked_beef")
    # 1, gudgeon: 1
    do_crafting("cooked_gudgeon")
    # 1, raw_chicken: 1
    do_crafting("cooked_chicken")

    # ======= FIGHTING ======

    # blue slime (6)
    print ("=== fight blue slime ===")
    x, y = 0, -2
    do_move(x, y)
    do_unequip("weapon")
    do_unequip("body_armor")
    #do_equip("wooden_staff", "weapon")
    do_equip("sticky_sword", "weapon")
    do_equip("copper_armor", "body_armor")
    cycle_fight(10)

    # green slime (4)
    print ("=== fight green slime ===")
    x, y = 3, -2
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


    # ======= BANKING ======

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    # just in case
    do_bank_deposit("ash_wood", 1)
    do_bank_deposit("ash_plank", 9)
    do_bank_deposit("spruce_plank", 4)
    do_bank_deposit("copper", 18)

    do_bank_deposit("feather", 4)
    do_bank_deposit("egg", 4)
    do_bank_deposit("raw_chicken", 4)
    do_bank_deposit("golden_egg", 1)
    do_bank_deposit("gudgeon", 4)
    do_bank_deposit("raw_beef", 4)

    do_bank_deposit("yellow_slimeball", 4)
    do_bank_deposit("green_slimeball", 4)
    do_bank_deposit("blue_slimeball", 4)
    do_bank_deposit("red_slimeball", 3)

    do_bank_deposit("cowhide", 2)

    do_bank_deposit("wooden_stick", 1)
    do_bank_deposit("wooden_shield", 1)
    do_bank_deposit("wooden_staff", 1)
    do_bank_deposit("copper_dagger", 1)
    do_bank_deposit("copper_helmet", 1)
    do_bank_deposit("copper_boots", 1)

    do_bank_deposit("copper_ring", 1)
    do_bank_deposit("life_amulet", 1)

    do_bank_deposit("feather_coat", 1)
    do_bank_deposit("copper_armor", 1)
    do_bank_deposit("copper_legs_armor", 1)
    do_bank_deposit("sticky_dagger", 1)
    do_bank_deposit("sticky_sword", 1)
    do_bank_deposit("water_bow", 1)
    do_bank_deposit("fire_staff", 1)
    do_bank_deposit("iron_dagger", 1)
    do_bank_deposit("greater_wooden_staff", 1)

    do_bank_deposit("cooked_gudgeon", 1)
    do_bank_deposit("cooked_chicken", 1)
    do_bank_deposit("cooked_beef", 1)
    do_bank_deposit("cooked_shrimp", 1)

    # equip changeable weapon and armor back
    do_bank_withdraw("sticky_dagger", 1)
    do_bank_withdraw("sticky_sword", 1)
    do_bank_withdraw("copper_armor", 1)
    do_bank_withdraw("feather_coat", 1)

