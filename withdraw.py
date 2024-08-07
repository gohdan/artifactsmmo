character_type = "main"

with open("functions.py") as functions:
    exec(functions.read())

print ("=== withdraw from bank ===")
x, y = 4, 1
do_move(x, y)

#do_bank_withdraw("ash_wood", 139)
#do_bank_withdraw("ash_plank", 16)
#do_bank_withdraw("copper_ore", 136)
#do_bank_withdraw("copper", 32)

#do_bank_withdraw("wooden_staff", 1)
#do_bank_withdraw("wooden_shield", 1)
#do_bank_withdraw("copper_helmet", 1)
#do_bank_withdraw("copper_boots", 1)

#do_bank_withdraw("feather_coat", 1)
#do_bank_withdraw("copper_armor", 1)
#do_bank_withdraw("copper_legs_armor", 1)
#do_bank_withdraw("sticky_dagger", 1)
#do_bank_withdraw("sticky_sword", 1)
#do_bank_withdraw("water_bow", 1)
#do_bank_withdraw("fire_staff", 1)

#do_bank_withdraw("iron_dagger", 1)

#do_bank_withdraw("copper_ring", 2)
#do_bank_withdraw("life_amulet", 1)

#do_bank_withdraw("cooked_gudgeon", 1)
#do_bank_withdraw("cooked_chicken", 1)

