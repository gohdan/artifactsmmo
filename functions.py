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
    max_hp = get_character_parameter(character, "max_hp")
    print ("max_hp: {}".format(max_hp))

    while True:
        hp = get_character_parameter(character, "hp")
        hp_diff = max_hp - hp

        print ("hp: {}".format(hp))
        print ("hp_diff: {}".format(hp_diff))

        if 0 != hp_diff:
            print ("hp < max_hp")
            inventory_items = get_inventory_items()
            print("inventory_items:{}".format(inventory_items))

            if "fried_eggs" in inventory_items or "cooked_beef" in inventory_items or "cooked_chicken" in inventory_items or "cooked_gudgeon" in inventory_items:
                print("have consumables, using to heal")
                match hp_diff:
                    case hp_diff if 1 <= hp_diff < 80:
                        if "cooked_chicken" in inventory_items:
                            use_item("cooked_chicken", 1)
                        elif "cooked_gudgeon" in inventory_items:
                            use_item("cooked_gudgeon", 1)
                    case hp_diff if 80 <= hp_diff :
                        if "cooked_beef" in inventory_items:
                            use_item("cooked_beef", 1)
                        elif "fried_eggs" in inventory_items:
                            use_item("fried_eggs", 1)
                        elif "cooked_chicken" in inventory_items:
                            use_item("cooked_chicken", 1)
                        elif "cooked_gudgeon" in inventory_items:
                           use_item("cooked_gudgeon", 1)
            else:
                print("have no consumables, do rest")
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

def do_bank_deposit_unnecessary(belongins):
    print ("*** do_bank_deposit_unnecessary")
    print ("belongings:{}".format(belongings))

    inventory = get_character_parameter(character, "inventory")
    print(inventory)

    for item in inventory:
        name = item['code']
        if "" != name:
            if name not in belongings:
                qty = item['quantity']
            else:
                qty = item['quantity'] - belongings[name]

            print("{} qty: {}".format(name, qty))
            if 0 < qty:
                print("do deposit:", name, qty)
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

    raw_data = f'{{"size" : "100"}}'

    response = requests.get(url, headers=headers, data=raw_data)

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

def do_unequip_all():

    print("*** do_unequip_all");

    slots = {'weapon', 'shield', 'helmet', 'body_armor', 'leg_armor', 'boots', 'ring1', 'ring2', 'amulet', 'artifact1', 'artifact2', 'artifact3', 'utility1', 'utility2', 'bag', 'rune'}

    for slot in slots:
        do_unequip(slot)

def do_bank_withdraw_belongings(belongings):

    print("*** do_bank_withdraw_belongings")

    bank_contents = get_bank_items()
    print (bank_contents)

    bank_items = {}
    for i in bank_contents:
        bank_items[i['code']] = i['quantity']

    print("bank_items:{}".format(bank_items))

    inventory_items = get_inventory_items()
    print("inventory_items:{}".format(inventory_items))

    print("belongings:{}".format(belongings))

    for item in belongings:
        print("item: {}".format(item))
        if item in inventory_items:
            print("item is in inventory, withdraw qty we don't have")
            qty = belongings[item] - inventory_items[item]
        else:
            print("item is not in inventory")
            if item in bank_items:
                print("item is in bank")
                print("item qty in bank:{}".format(bank_items[item]))
                if belongings[item] <= bank_items[item]:
                    print("there is enough qty in bank")
                    qty = belongings[item]
                else:
                    print("there is not enough qty in bank")
                    qty = bank_items[item]
            else:
                print("item is not in bank")
                qty = 0

        print("{}: {}".format(item, qty))
        if 0 < qty:
            print("withdraw {}: {}".format(item, qty))
            do_bank_withdraw(item, qty)


def do_equip_to_monster(monster):

    print("*** do_equip_to_monster")

    print("monster:{}".format(monster))

    do_unequip_all()

    inventory = get_character_parameter(character, "inventory")
    print(inventory)

    inventory_items = {}
    for item in inventory:
        inventory_items[item['code']] = item['quantity']

    print("inventory_items:{}".format(inventory_items))

    match monster:
        case monster if "chicken" == monster:
            if "sticky_sword" in inventory_items:
                do_equip("sticky_sword", "weapon")
            elif "wooden_staff" in inventory_items:
                do_equip("wooden_staff", "weapon")
            elif "copper_dagger" in inventory_items:
                do_equip("copper_dagger", "weapon")
            elif "wooden_stick" in inventory_items:
                do_equip("wooden_stick", "weapon")

            if "copper_armor" in inventory_items:
                do_equip("copper_armor", "body_armor")

            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring1")
            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring2")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility1")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility2")

            if "wooden_shield" in inventory_items:
                do_equip("wooden_shield", "shield")
            if "copper_legs_armor" in inventory_items:
                do_equip("copper_legs_armor", "leg_armor")
            if "copper_boots" in inventory_items:
                do_equip("copper_boots", "boots")
            if "copper_helmet" in inventory_items:
                do_equip("copper_helmet", "helmet")
            if "life_amulet" in inventory_items:
                do_equip("life_amulet", "amulet")

        case monster if "yellow_slime" == monster:
            # 25% Res Earth

            if "sticky_dagger" in inventory_items:
                do_equip("sticky_dagger", "weapon")
            if "copper_dagger" in inventory_items:
                do_equip("copper_dagger", "weapon")
            elif "wooden_staff" in inventory_items:
                do_equip("wooden_staff", "weapon")
            elif "wooden_stick" in inventory_items:
                do_equip("wooden_stick", "weapon")

            if "feather_coat" in inventory_items:
                do_equip("feather_coat", "body_armor")
            elif "copper_armor" in inventory_items:
                do_equip("copper_armor", "body_armor")

            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring1")
            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring2")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility1")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility2")

            if "wooden_shield" in inventory_items:
                do_equip("wooden_shield", "shield")
            if "copper_legs_armor" in inventory_items:
                do_equip("copper_legs_armor", "leg_armor")
            if "copper_boots" in inventory_items:
                do_equip("copper_boots", "boots")
            if "copper_helmet" in inventory_items:
                do_equip("copper_helmet", "helmet")
            if "life_amulet" in inventory_items:
                do_equip("life_amulet", "amulet")

        case monster if "green_slime" == monster:
            # 25% Res Air

            if "sticky_sword" in inventory_items:
                do_equip("sticky_sword", "weapon")
            elif "wooden_staff" in inventory_items:
                do_equip("wooden_staff", "weapon")
            elif "sticky_dagger" in inventory_items:
                do_equip("sticky_dagger", "weapon")
            elif "copper_dagger" in inventory_items:
                do_equip("copper_dagger", "weapon")
            elif "wooden_stick" in inventory_items:
                do_equip("wooden_stick", "weapon")

            if "copper_armor" in inventory_items:
                do_equip("copper_armor", "body_armor")
            elif "feather_coat" in inventory_items:
                do_equip("feather_coat", "body_armor")

            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring1")
            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring2")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility1")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility2")

            if "wooden_shield" in inventory_items:
                do_equip("wooden_shield", "shield")
            if "copper_legs_armor" in inventory_items:
                do_equip("copper_legs_armor", "leg_armor")
            if "copper_boots" in inventory_items:
                do_equip("copper_boots", "boots")
            if "copper_helmet" in inventory_items:
                do_equip("copper_helmet", "helmet")
            if "life_amulet" in inventory_items:
                do_equip("life_amulet", "amulet")

        case monster if "blue_slime" == monster:
            # 25% Res Water

            if "sticky_sword" in inventory_items:
                do_equip("sticky_sword", "weapon")
            elif "sticky_dagger" in inventory_items:
                do_equip("sticky_dagger", "weapon")
            elif "copper_dagger" in inventory_items:
                do_equip("copper_dagger", "weapon")
            elif "wooden_staff" in inventory_items:
                do_equip("wooden_staff", "weapon")
            elif "wooden_stick" in inventory_items:
                do_equip("wooden_stick", "weapon")

            if "copper_armor" in inventory_items:
                do_equip("copper_armor", "body_armor")
            elif "feather_coat" in inventory_items:
                do_equip("feather_coat", "body_armor")

            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring1")
            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring2")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility1")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility2")

            if "wooden_shield" in inventory_items:
                do_equip("wooden_shield", "shield")
            if "copper_legs_armor" in inventory_items:
                do_equip("copper_legs_armor", "leg_armor")
            if "copper_boots" in inventory_items:
                do_equip("copper_boots", "boots")
            if "copper_helmet" in inventory_items:
                do_equip("copper_helmet", "helmet")
            if "life_amulet" in inventory_items:
                do_equip("life_amulet", "amulet")

        case monster if "red_slime" == monster:
            # 25% Res Fire

            if "water_bow" in inventory_items:
                do_equip("water_bow", "weapon")
            elif "sticky_sword" in inventory_items:
                do_equip("sticky_sword", "weapon")
            elif "sticky_dagger" in inventory_items:
                do_equip("sticky_dagger", "weapon")
            elif "copper_dagger" in inventory_items:
                do_equip("copper_dagger", "weapon")
            elif "wooden_staff" in inventory_items:
                do_equip("wooden_staff", "weapon")
            elif "wooden_stick" in inventory_items:
                do_equip("wooden_stick", "weapon")

            if "feather_coat" in inventory_items:
                do_equip("feather_coat", "body_armor")
            elif "copper_armor" in inventory_items:
                do_equip("copper_armor", "body_armor")

            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring1")
            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring2")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility1")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility2")

            if "wooden_shield" in inventory_items:
                do_equip("wooden_shield", "shield")
            if "copper_legs_armor" in inventory_items:
                do_equip("copper_legs_armor", "leg_armor")
            if "copper_boots" in inventory_items:
                do_equip("copper_boots", "boots")
            if "copper_helmet" in inventory_items:
                do_equip("copper_helmet", "helmet")
            if "life_amulet" in inventory_items:
                do_equip("life_amulet", "amulet")

        case monster if "cow" == monster:
            # -30% Res Earth, 30% Res Water

            if "sticky_sword" in inventory_items:
                do_equip("sticky_sword", "weapon")
            elif "wooden_staff" in inventory_items:
                do_equip("wooden_staff", "weapon")
            elif "wooden_stick" in inventory_items:
                do_equip("wooden_stick", "weapon")

            if "copper_armor" in inventory_items:
                do_equip("copper_armor", "body_armor")
            elif "feather_coat" in inventory_items:
                do_equip("feather_coat", "body_armor")

            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring1")
            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring2")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility1")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility2")

            if "wooden_shield" in inventory_items:
                do_equip("wooden_shield", "shield")
            if "copper_legs_armor" in inventory_items:
                do_equip("copper_legs_armor", "leg_armor")
            if "copper_boots" in inventory_items:
                do_equip("copper_boots", "boots")
            if "copper_helmet" in inventory_items:
                do_equip("copper_helmet", "helmet")
            if "life_amulet" in inventory_items:
                do_equip("life_amulet", "amulet")

        case monster if "mushmush" == monster:
            # -30% Res Earth, 30% Res Water

            if "sticky_dagger" in inventory_items:
                do_equip("sticky_dagger", "weapon")
            if "copper_dagger" in inventory_items:
                do_equip("copper_dagger", "weapon")
            elif "wooden_staff" in inventory_items:
                do_equip("wooden_staff", "weapon")
            elif "wooden_stick" in inventory_items:
                do_equip("wooden_stick", "weapon")

            if "feather_coat" in inventory_items:
                do_equip("feather_coat", "body_armor")
            elif "copper_armor" in inventory_items:
                do_equip("copper_armor", "body_armor")

            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring1")
            if "copper_ring" in inventory_items:
                do_equip("copper_ring", "ring2")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility1")
            if "small_health_potion" in inventory_items:
                do_equip("small_health_potion", "utility2")

            if "wooden_shield" in inventory_items:
                do_equip("wooden_shield", "shield")
            if "copper_legs_armor" in inventory_items:
                do_equip("copper_legs_armor", "leg_armor")
            if "copper_boots" in inventory_items:
                do_equip("copper_boots", "boots")
            if "copper_helmet" in inventory_items:
                do_equip("copper_helmet", "helmet")
            if "life_amulet" in inventory_items:
                do_equip("life_amulet", "amulet")

def get_inventory_items():

    print("*** get_inventory_items")

    inventory = get_character_parameter(character, "inventory")
    print(inventory)

    inventory_items = {}
    for item in inventory:
        inventory_items[item['code']] = item['quantity']

    print("inventory_items:{}".format(inventory_items))

    return inventory_items

def get_item_in_bank_qty(item):

    print("*** get_item_in_bank_qty")

    bank_contents = get_bank_items()
    print (bank_contents)

    bank_items = {}
    for i in bank_contents:
        bank_items[i['code']] = i['quantity']

    print("bank_items:{}".format(bank_items))

    if item in bank_items:
        qty = bank_items[item]
    else:
        qty = 0
    print("qty: {}".format(qty))

    return qty

def if_requisites_available(requisites, bank_items, inventory_available):

    print("*** if_requisites_available")

    print("requisites: {}".format(requisites))
    print("bank_items: {}".format(bank_items))
    print("inventory_available: {}".format(inventory_available))

    requisites_available = 1
    requisites_qty = 0

    for requisite in requisites:
        print("requisite: {}".format(requisite))
        if requisite in bank_items:
            print("have {}: {} in bank".format(requisite, requisites[requisite]))
            requisites_qty += requisites[requisite]
            if requisites[requisite] > bank_items[requisite]:
                print("not enough requisite in bank")
                requisites_available = 0
            if requisites_qty > inventory_available:
                print("not enought space in inventory for all requisites")
                requisites_available = 0
        else:
            print("don't have {} in bank".format(requisite))
            requisites_available = 0

    return requisites_available

def use_item(name, qty):
    print ("use item")

    print("name: {}, qty: {}".format(name, qty))

    url = f"{server}/my/{character}/action/use"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    raw_data = f'{{"code" : {name}, "quantity": {qty}}}'

    response = requests.post(url, headers=headers, data=raw_data)

    cooldown = 1

    if response.status_code == 404:
        print("Item not found")
    elif response.status_code == 476:
        print("This item is not a consumable")
    elif response.status_code == 478:
        print("Missing item or insufficient quantity")
    elif response.status_code == 486:
        print("An action is already in progress by your character")
    elif response.status_code == 496:
        print("Character level is insufficient")
    elif response.status_code == 498:
        print("Character not found")
    elif response.status_code == 499:
        print("Character in cooldown")
        cooldown = buy_bank_expansion(x, y);
    elif response.status_code != 200:
        print("An error occured while doing api request")
        print("status code:", response.status_code)
    else:
        print("Request successful")
        data = response.json()["data"]
        cooldown = data["cooldown"]["total_seconds"]

    print("Cooldown:", cooldown)
    if cooldown is None:
        print("cooldown is None, setting it to 60")
        cooldown = 60
        print("Cooldown:", cooldown)

    time.sleep(cooldown)

