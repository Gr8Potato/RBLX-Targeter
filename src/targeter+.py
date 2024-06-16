'''
======================
By: Gr8P0tat0
Last Modified: 14JUN24
======================
'''

import requests
import time
import sys

perm_spectre_targets = ["41uis", "Expiral", "daxlovescars", 'Acrynax', 'finalnickADD', 'Kurashina_lzumi', 'vTakina', 'Te0Void', 'Tim_NightShade', 'Caonalyst', 'snellejelte', 'Guy_Broman', 'ReiAstra', 'flem_sy', 'JBF3', 'KolegaPolakYT', 'Pieface1091']
phantom_spectre_targets = ["RisenVezyr"]

perm_spectre_groups = {
    "Nighthawk Combat Engineers: Leviathan": 33391710,
    "Nighthawk Imperial Peacekeeper Corps": 4543661
}

phantom_spectre_groups = {
    "Nighthawk Manticore": 15026315
}

perm_spectre_roles = {
    4486074: [
        "| O | Drill Sergeant",
        "| O | Ultra",
        "| C | Council",
        "| C | Captain-Major",
        "| X | Chief Superintendent",
        "| X | Commandant",
        "| X | Deputy Chief",
        "| X | Chief",
        "| X | Overseer",
        "| X | Administration",
        "| X | Commander",
        "| X | Viceroy"
    ],
    15026315: [
        "Operative",
        "Senior Operative",
        "Elite",
        "Auxilior",
        "Zealot",
        "Kaidon",
        "Chief Superintendent",
        "Arbiter",
        "Deputy Chief",
        "Chief",
        "Administration",
        "Viceroy"
    ],
    1174414: [
        "| C | Commodore",
        "| HC | Admiral",
        "| HC | Arch Admiral",
        "| X | Supreme Admiral",
        "| X | Commander",
        "| X | Viceroy"
    ],
    3497000: [
        "Royal Officer",
        "High Command",
        "Director",
        "Overseer",
        "Administration",
        "Commander",
        "Viceroy"
    ],
    4809530: [
        "| HC | Ordinatus",
        "| HC | Praefectus",
        "| X | Fabricator-General",
        "| X | Overseer",
        "| X | Administration",
        "| X | Viceroy"
    ],
    3496996: [
        "Commandant",
        "Advisor",
        "Deputy Director",
        "Director",
        "Overseer",
        "Administration",
        "Commander",
        "Viceroy"
    ],
    3497030: [
        "| HC | Chief Superintendent",
        "| HC | Deputy Chief",
        "| C | Chief",
        "| X | Overseer",
        "| X | Commander",
        "| X | Administration",
        "| X | Viceroy"
    ],
    4734688: [
        "Arbiter",
        "Warden",
        "Director",
        "Overseer",
        "Commander",
        "Administration",
        "Viceroy"
    ],
    3612873: [
        "C | Council",
        "C | Consul",
        "Forerunner",
        "Overseer",
        "Administration",
        "Commander",
        "Viceroy"
    ]
}

phantom_spectre_roles = {}

def search_users(session, keyword, use_countdown):
    print("-" * 40)
    url = f"https://users.roblox.com/v1/users/search?keyword={keyword}&limit=100"
    response = make_request(session, url)

    if response:
        data = response.json()
        users = data.get('data', [])
        found_user = False

        for user in users:
            if user['name'].lower() == keyword.lower():
                found_user = True
                print(f"Username: {user['name']}, DisplayName: {user['displayName']}, Id: {user['id']}")
                print("-" * 40)
                is_target = False

                if user['name'].lower() in [u.lower() for u in perm_spectre_targets]:
                    print(f"{user['name']} | Permanent Hit")
                    is_target = True

                if user['name'].lower() in [u.lower() for u in phantom_spectre_targets]:
                    print(f"{user['name']} | Phantom Assigned")
                    is_target = True

                fetch_user_groups(session, user['id'], user['name'], is_target, use_countdown)
                break

        if not found_user:
            print(f"No exact match found for username: {keyword}")
    else:
        print(f"Failed to retrieve users.")

def fetch_user_groups(session, user_id, username, is_target, use_countdown):
    url = f"https://groups.roblox.com/v1/users/{user_id}/groups/roles"
    response = make_request(session, url)

    if response:
        data = response.json()
        groups = data.get('data', [])

        in_nighthawk_imperium = False

        for group in groups:
            group_id = group['group']['id']
            group_name = group['group']['name']
            role_name = group['role']['name']

            if group_id == 1174414:
                in_nighthawk_imperium = True

            if group_id in perm_spectre_groups.values():
                print(f"{group_name}, {username} | Permanent Hit")
                is_target = True

            if group_id in phantom_spectre_groups.values():
                print(f"{group_name}, {username} | Phantom Assigned")
                is_target = True

            if group_id in perm_spectre_roles and role_name in perm_spectre_roles[group_id]:
                print(f"{group_name}, {role_name}, {username} | Permanent Hit")
                is_target = True

            if group_id in phantom_spectre_roles and role_name in phantom_spectre_roles[group_id]:
                print(f"{group_name}, {role_name}, {username} | Phantom Assigned")
                is_target = True

        if not in_nighthawk_imperium:
            is_target = False
            print(f"{username} is not in The Nighthawk Imperium. Not a target. Are you sure you typed the name in correctly?")

        if not is_target:
            print(f"No target roles or groups of interest found for User ID {user_id}.")
    else:
        print(f"Failed to retrieve groups for User ID {user_id}: {response.status_code}")
    if use_countdown:
        countdown(60)

def make_request(session, url):
    response = session.get(url)
    if response.status_code == 200:
        return response
    else:
        print(f"Request failed with status code: {response.status_code}")
        countdown(60)
        return None

def countdown(seconds):
    print("=" * 40)
    for i in range(seconds, -1, -1):
        sys.stdout.write(f"\rCooldown: {i} seconds remaining ")
        sys.stdout.flush()
        time.sleep(1)
    print("\r")

if __name__ == "__main__":
    session = requests.Session()
    print("=" * 40)
    cookie = input("Enter .ROBLOSECURITY cookie (or leave blank to skip): ")
    print("=" * 40)
    use_countdown = not cookie
    if cookie:
        session.headers.update({'Cookie': f'.ROBLOSECURITY={cookie}'})
    while True:
        search_term = input("Enter user: ")
        search_users(session, search_term, use_countdown)
        print("=" * 40)