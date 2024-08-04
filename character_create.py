with open("functions.py") as functions:
    exec(functions.read())

print ("=== character creation ===")

# character name: >= 3 characters<= 12 characters, pattern ^[a-zA-Z0-9_-]+$
# skins: men1, men2, men3, women1, women2, women3

character_name="YourDesiredCharacterName"
skin="YourDesiredCharacterSkin"

url = f"{server}/characters/create"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

raw_data = f'{{"name" : "{character_name}", "skin": "{skin}"}}'
print("raw data:", raw_data)

response = requests.post(url, headers=headers, data=raw_data)

cooldown = 60

if response.status_code == 494:
    print("Name already used")
elif response.status_code == 495:
    print("Maximum characters reached on your account")
elif response.status_code != 200:
    print("An error occured while doing api request")
    print("status code:", response.status_code)
else:
    print("Character creation successful")


