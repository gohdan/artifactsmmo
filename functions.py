import requests
import time
import json
from collections import OrderedDict

with open("_auth_data.py") as auth_data:
    exec(auth_data.read())

# _auth_data.py template:
# token = "your_api_token"
# characters = {
#     'main': "Name1",
#     'carpenter': "Name2",
#     'miner': "Name3",
#     'fisher': "Name4",
#     'crafter': "Name5"
#}

character_type = character_type if 'character_type' in locals() else 'main'
print("character_type:", character_type)
character = characters[character_type]
print("character:", character)

server = "https://api.artifactsmmo.com"

cooldown = 60

def do_move(x, y):

    print("moving to x:", x, ", y:", y)
    url = f"{server}/my/{character}/action/move"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    raw_data = f'{{"x" : {x}, "y": {y}}}'

    response = requests.post(url, headers=headers, data=raw_data)

    cooldown = 60

    if response.status_code == 404:
        print("Map not found")
    elif response.status_code == 486:
        print("Character is locked. Action is already in progress")
    elif response.status_code == 490:
        print("Character already at destination")
        cooldown = 0;
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = do_move(x, y);
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
        cooldown = do_move(x, y);
    else:
        print("Move successful")
        data = response.json()["data"]
        cooldown = data["cooldown"]["total_seconds"]

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown)

    time.sleep(cooldown)

def do_gathering():
    url = f"{server}/my/{character}/action/gathering"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, headers=headers)

    cooldown = 60

    if response.status_code == 486:
        print("Character is locked. Action is already in progress")
    elif response.status_code == 493:
        print("Not skill level required")
    elif response.status_code == 497:
        print("Inventory is full")
        cooldown = 0
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = do_gathering();
    elif response.status_code == 598:
        print("Resource not found on this map")
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Gathering successful")
        data = response.json()["data"]
        cooldown = data["cooldown"]["total_seconds"]

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown);

    time.sleep(cooldown)

def do_fight():

    while True:
        hp = get_character_parameter(character, "hp")
        max_hp = get_character_parameter(character, "max_hp")

        print ("hp:", hp)
        print ("max_hp:", max_hp)

        if hp < max_hp:
            print ("hp < max_hp, do rest")
            do_rest(character)
        else:
            break

    url = f"{server}/my/{character}/action/fight"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, headers=headers)

    cooldown = 60

    if response.status_code == 497:
        print("Inventory is full")

    if response.status_code == 486:
        print("Character is locked. Action is already in progress")
    elif response.status_code == 497:
        print("Character inventory is full")
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = do_fight();
    elif response.status_code == 598:
        print("Monster not found on this map")
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Fight ended")
        data = response.json()["data"]
        cooldown = data["cooldown"]["total_seconds"]
        fight_result = data["fight"]["result"]
        print("Fight result:", fight_result);

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown);

    time.sleep(cooldown)

def do_bank_deposit(item, qty):

    print("item: {}, qty: {}".format(item,qty))

    if "gold" == item:
        url = f"{server}/my/{character}/action/bank/deposit/gold"
        raw_data = f'{{"quantity": {qty}}}'
    else:
        url = f"{server}/my/{character}/action/bank/deposit"
        raw_data = f'{{"code" : "{item}", "quantity": {qty}}}'

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, headers=headers, data=raw_data)

    cooldown = 1

    if response.status_code == 404:
        print("Item not found")
    elif response.status_code == 422:
        print("Unprocessible query")
    elif response.status_code == 462:
        print("Bank is full")
    elif response.status_code == 478:
        print("Missing item or insufficient quantity in your inventory")
    elif response.status_code == 486:
        print("Character is locked. Action is already in progress")
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = do_bank_deposit(x, y);
    elif response.status_code == 598:
        print("Bank not found on this map")
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Deposit successful")
        data = response.json()["data"]
        print(*data["bank"], sep='\n')
        cooldown = data["cooldown"]["total_seconds"]

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown)

    time.sleep(cooldown)

def do_bank_withdraw(item, qty):
    print("do_bank_withdraw")

    print("item: {}, qty: {}".format(item,qty))

    if "gold" == item:
        url = f"{server}/my/{character}/action/bank/withdraw/gold"
        raw_data = f'{{"quantity": {qty}}}'
    else:
        url = f"{server}/my/{character}/action/bank/withdraw"
        raw_data = f'{{"code" : "{item}", "quantity": {qty}}}'

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, headers=headers, data=raw_data)

    cooldown = 1

    if response.status_code == 404:
        print("Item not found")
    elif response.status_code == 478:
        print("Missing item or insufficient quantity in your inventory")
    elif response.status_code == 486:
        print("Character is locked. Action is already in progress")
    elif response.status_code == 497:
        print("Character inventory is full")        
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = do_bank_withdraw(item, qty);
    elif response.status_code == 598:
        print("Bank not found on this map")
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Withdraw successful")
        data = response.json()["data"]
        print(*data["bank"], sep='\n')
        cooldown = data["cooldown"]["total_seconds"]

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown)

    time.sleep(cooldown)

def do_unequip(slot):

    print("slot:", slot)
    url = f"{server}/my/{character}/action/unequip"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    raw_data = f'{{"slot" : "{slot}"}}'

    response = requests.post(url, headers=headers, data=raw_data)

    cooldown = 1

    if response.status_code == 404:
        print("Item not found")
    elif response.status_code == 486:
        print("Character is locked. Action is already in progress")
    elif response.status_code == 491:
        print("Slot is empty")
    elif response.status_code == 497:
        print("Character inventory is full")        
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = do_unequip(slot);
    elif response.status_code == 598:
        print("Bank not found on this map")
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Unequip successful")
        data = response.json()["data"]
        #print(*data["item"], sep='\n')
        cooldown = data["cooldown"]["total_seconds"]

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown)

    time.sleep(cooldown)

def do_equip(code, slot):

    print("code:", code)
    print("slot:", slot)
    url = f"{server}/my/{character}/action/equip"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    raw_data = f'{{"code" : "{code}", "slot" : "{slot}"}}'

    response = requests.post(url, headers=headers, data=raw_data)

    cooldown = 1

    if response.status_code == 404:
        print("Item not found")
    elif response.status_code == 478:
        print("Missing item or insufficient quantity in your inventory")
    elif response.status_code == 485:
        print("This item is already equipped")
    elif response.status_code == 486:
        print("Character is locked. Action is already in progress")
    elif response.status_code == 491:
        print("Slot is not empty")
    elif response.status_code == 496:
        print("Character level is insufficient")
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = do_equip(slot);
    elif response.status_code == 598:
        print("Bank not found on this map")
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Equip successful")
        data = response.json()["data"]
        #print(*data["item"], sep='\n')
        cooldown = data["cooldown"]["total_seconds"]

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown)

    time.sleep(cooldown)

def do_crafting(code):

    print("code:", code)
    url = f"{server}/my/{character}/action/crafting"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    raw_data = f'{{"code" : "{code}"}}'

    response = requests.post(url, headers=headers, data=raw_data)

    cooldown = 1

    if response.status_code == 404:
        print("Item not found")
    elif response.status_code == 478:
        print("Missing item or insufficient quantity in your inventory")
    elif response.status_code == 486:
        print("Character is locked. Action is already in progress")
    elif response.status_code == 493:
        print("Not skill level required")
    elif response.status_code == 497:
        print("Character inventory is full")        
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = do_crafting(code);
    elif response.status_code == 598:
        print("Workshop not found on this map")
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Crafting successful")
        data = response.json()["data"]
        print(*data["details"]["items"], sep='\n')
        cooldown = data["cooldown"]["total_seconds"]

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown)

    time.sleep(cooldown)

def cycle_gathering(iterations):
    for i in range (iterations):
      i_human = i+1
      print("gathering", i_human, "/", iterations)
      do_gathering()

def cycle_fight(iterations):
    for i in range (iterations):
      i_human = i+1
      #print("equip consumables")
      #do_equip("cooked_shrimp", "consumable1")
      #do_equip("cooked_beef", "consumable1")
      #do_equip("cooked_chicken", "consumable1")
      #do_equip("cooked_gudgeon", "consumable1")
      #do_equip("cooked_shrimp", "consumable2")
      #do_equip("cooked_beef", "consumable2")
      #do_equip("cooked_chicken", "consumable2")
      #do_equip("cooked_gudgeon", "consumable2")
      print("fight {} / {}".format(i_human, iterations))
      do_fight()

def cycle_crafting(code, iterations):
    for i in range (iterations):
      i_human = i+1
      print("craft", code, i_human, "/", iterations)
      do_crafting(code)

def get_characters_array():

    print("*** get characters array")
    url = f"{server}/my/characters"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
        return 0
    else:
        print("Request successful")
        data = response.json()["data"]
        return data

def get_character_parameter(char_name, parameter):

    print ("*** get character parameter")
    print ("character name: ", char_name)
    print ("parameter: ", parameter)

    param = ""
    data = get_characters_array()

    for char in data:
        name = char['name']
        if name == char_name:
            param = char[parameter]
            print (name, parameter, ":", param)
            break

    return param;

def do_rest(character):

    print("character:", character)
    url = f"{server}/my/{character}/action/rest"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, headers=headers)

    cooldown = 1

    if response.status_code == 486:
        print("Character is locked. Action is already in progress")
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = do_equip(slot);
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Rest successful")
        data = response.json()["data"]
        cooldown = data["cooldown"]["total_seconds"]

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown)

    time.sleep(cooldown)

def do_bank_deposit_unnecessary(inventory, belongins):
    print ("*** do_bank_deposit_unnecessary")
    print ("belongings:", belongings)
    print ("inventory:", inventory)

    for item in inventory:
        name = item['code']
        if "" != name and name not in belongings:
            qty = item['quantity']
            print ("do deposit:", name, qty)
            do_bank_deposit(name, qty)

def get_bank_info():
    print("*** get_bank_info")

    url = f"{server}/my/bank"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    data = ""

    if response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Request successful")
        data = response.json()["data"]
        print(*data, sep='\n')
        #cooldown = data["cooldown"]["total_seconds"]

    return data

def get_bank_items():
    print("*** get_bank_items")

    url = f"{server}/my/bank/items"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    data = ""

    if response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Request successful")
        data = response.json()["data"]
        print(*data, sep='\n')

    return data
def buy_bank_expansion():
    print ("buy bank expansion")

    url = f"{server}/my/{character}/action/bank/buy_expansion"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(url, headers=headers)

    cooldown = 1

    if response.status_code == 486:
        print("Character is locked. Action is already in progress")
    elif response.status_code == 492:
        print("Insufficient gold on character")
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = buy_bank_expansion(x, y);
    elif response.status_code == 598:
        print("Bank not found on this map")
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Request successful")
        data = response.json()["data"]
        print(*data["transaction"], sep='\n')
        cooldown = data["cooldown"]["total_seconds"]

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown)

    time.sleep(cooldown)
