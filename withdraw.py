
with open("functions.py") as functions:
    exec(functions.read())

print ("=== withdraw from bank ===")
x, y = 4, 1
do_move(x, y)

#do_bank_withdraw("ash_wood", 139)
#do_bank_withdraw("ash_plank", 16)
#do_bank_withdraw("copper_ore", 136)
#do_bank_withdraw("copper", 32)
#do_bank_withdraw("wooden_shield", 2)
#do_bank_withdraw("wooden_staff", 1)

