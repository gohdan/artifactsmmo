character_type = "miner"

with open("functions.py") as functions:
    exec(functions.read())

print("=== craft ruby ===")

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw ruby_stone")
do_bank_withdraw("ruby_stone", 24)

print("move to workshop mining")
x, y = 1, 5
do_move(x, y)

do_crafting("ruby")

