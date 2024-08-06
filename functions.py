import requests
import time
import json

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

    print("item:", item,", qty:", qty)
    url = f"{server}/my/{character}/action/bank/deposit"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    raw_data = f'{{"code" : "{item}", "quantity": {qty}}}'

    response = requests.post(url, headers=headers, data=raw_data)

    cooldown = 1

    if response.status_code == 404:
        print("Item not found")
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

    print("item:", item,", qty:", qty)
    url = f"{server}/my/{character}/action/bank/withdraw"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    raw_data = f'{{"code" : "{item}", "quantity": {qty}}}'

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
      print("equip consumables")
      do_equip("cooked_beef", "consumable1")
      do_equip("cooked_chicken", "consumable1")
      do_equip("cooked_gudgeon", "consumable1")
      do_equip("cooked_beef", "consumable2")
      do_equip("cooked_chicken", "consumable2")
      do_equip("cooked_gudgeon", "consumable2")
      print("fight", i_human, "/", iterations)
      do_fight()

def cycle_crafting(code, iterations):
    for i in range (iterations):
      i_human = i+1
      print("craft", code, i_human, "/", iterations)
      do_crafting(code)

