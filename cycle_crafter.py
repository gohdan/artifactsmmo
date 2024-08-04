character_type ="crafter"

with open("functions.py") as functions:
    exec(functions.read())

print("=== crafter cycle ===")

# 1 cycle of wood - ash_wood 40 (ash_plank 6, ash_wood 4)
# 1 cycle of copper - copper_ore 78 (copper 13)

print("move to bank")
x, y = 4, 1
do_move(x, y)

print("withdraw ash wood")
do_bank_withdraw("ash_wood", 40)

print("withdraw copper ore")
do_bank_withdraw("copper_ore", 78)

# print("withdraw copper")
# do_bank_withdraw("copper", 30)



print("move to workshop woodcutting")
x, y = -2, -3
do_move(x, y)

# ash_wood: 6
for i in range (6):
    do_crafting("ash_plank")

print("move to workshop mining")
x, y = 1, 5
do_move(x, y)

# copper_ore: 13
for i in range (13):
    do_crafting("copper")

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
