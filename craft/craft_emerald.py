character_type = "miner"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft emerald ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw emerald_stone")
do_bank_withdraw("emerald_stone", 24)

print("move to workshop mining")
x, y = 1, 5
do_move(x, y)

do_crafting("emerald")

