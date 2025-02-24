character_type = "main"

with open("functions.py") as functions:
    exec(functions.read())

print ("=== get characters ===")

data = get_characters_array()

print(json.dumps(data, indent=4))

