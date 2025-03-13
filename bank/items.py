character_type = "crafter"

with open("functions.py") as functions:
    exec(functions.read())

# bank
print ("=== deposit to bank ===")
x, y = 4, 1
do_move(x, y)

bank_contents = get_bank_items()
print (bank_contents)

