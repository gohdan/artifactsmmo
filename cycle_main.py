character_type ="main"

with open("functions.py") as functions:
    exec(functions.read())

while True:

    # ======= FIGHTING ======

    ## flying serpent (10)
    #print ("=== fight flying serpent ===")
    #x, y = 5, 4
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    #do_equip("greater_wooden_staff", "weapon")
    #do_equip("feather_coat", "body_armor")
    #cycle_fight(10)

    ## mushmush (10)
    #print ("=== fight mushmush ===")
    #x, y = 5, 3
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    #do_equip("iron_dagger", "weapon")
    #do_equip("feather_coat", "body_armor")
    #cycle_fight(10)

    # cow (8)
    #print ("=== fight cow ===")
    #x, y = 0, 2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("sticky_sword", "weapon")
    #do_equip("iron_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    #cycle_fight(10)
    
    ## red slime (7)
    #print ("=== fight red slime ===")
    #x, y = 2, -2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("sticky_sword", "weapon")
    #do_equip("iron_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    #cycle_fight(10)

    # blue slime (6)
    #print ("=== fight blue slime ===")
    #x, y = 0, -2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("wooden_staff", "weapon")
    #do_equip("sticky_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    #cycle_fight(10)

    # green slime (4)
    #print ("=== fight green slime ===")
    #x, y = 3, -2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("wooden_staff", "weapon")
    #do_equip("sticky_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    #cycle_fight(10)

    # yellow slime (2)
    #print ("=== fight yellow slime ===")
    #x, y = 1, -2
    #do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("copper_dagger", "weapon")
    ##do_equip("sticky_dagger", "weapon")
    #do_equip("iron_dagger", "weapon")
    #do_equip("feather_coat", "body_armor")
    #cycle_fight(10)

    # chicken (1)
    print ("=== fight chicken ===")
    x, y = 0, 1
    do_move(x, y)
    #do_unequip("weapon")
    #do_unequip("body_armor")
    ##do_equip("wooden_staff", "weapon")
    #do_equip("sticky_sword", "weapon")
    #do_equip("copper_armor", "body_armor")
    cycle_fight(10)

    # ======= BANKING ======

    # bank
    print ("=== bank ===")
    x, y = 4, 1
    do_move(x, y)

    do_bank_deposit("feather", 5)
    do_bank_deposit("egg", 5)
    do_bank_deposit("raw_chicken", 5)
    do_bank_deposit("golden_egg", 1)

    #do_bank_deposit("yellow_slimeball", 5)
    #do_bank_deposit("green_slimeball", 5)
    #do_bank_deposit("blue_slimeball", 5)
    #do_bank_deposit("red_slimeball", 5)
    #do_bank_deposit("raw_beef", 5)
    #do_bank_deposit("milk_bucket", 5)
    #do_bank_deposit("cowhide", 5)
    #do_bank_deposit("mushroom", 5)
    #do_bank_deposit("flying_wing", 1)
    #do_bank_deposit("serpent_skin", 1)

    #do_bank_withdraw("cooked_beef", 10)
    #do_bank_withdraw("cooked_chicken", 10)
    #do_bank_withdraw("cooked_gudgeon", 10)

