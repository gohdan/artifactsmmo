character_type = "miner"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft topaz ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw topaz_stone")
do_bank_withdraw("topaz_stone", 24)

print("move to workshop mining")
x, y = 1, 5
do_move(x, y)

do_crafting("topaz")

