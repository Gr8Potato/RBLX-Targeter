'''
======================
By: Gr8P0tat0
Last Modified: 17JUN24
======================
LEGAL NOTICE: ANY SIGNIFICANT
INSPIRATION/ALTERCATIONS OF
MY CODE MUST BE MADE OPEN
SOURCE PER THE GNU GENERAL
PUBLIC LICENSE Version 3.
======================
'''

import requests
import time
import sys

'''
If you're updating this yourself:

Groups: Name: ID
Roles: ID: Name(s)
Morphs: ID: Name
'''

'''
REFERENCE SHEET

nighthawk_groups = {
    "Nighthawk Combat Engineers": 4809530,
    "Nighthawk Combat Engineers: Leviathan": 33391710,
    "Nighthawk Commandos": 3496996,
    "Nighthawk Commandos: Ghosts": 11000162,
    "Nighthawk Guardians": 4183818,
    "Nighthawk Imperial Peacekeeper Corps": 4543661,
    "Nighthawk Imperium": 1174414,
    "Nighthawk Integration Department": 8244715,
    "Nighthawk Manticore": 15026315,
    "Nighthawk Military Police": 3497030,
    "Nighthawk Military Police: Cerberus": 4486074,
    "Nighthawk Reaper Battalion": 4734688,
    "Nighthawk Reaper Battalion: Black Daggers": 4936035,
    "Nighthawk Royal Guards": 3497000,
    "Nighthawk Vanguards": 3612873
}
'''

# SPECTRES
perm_spectre_targets = ["41uis", "Expiral", "daxlovescars", 'Acrynax', 'finalnickADD', 'Kurashina_lzumi', 'vTakina', 'Te0Void', 'Tim_NightShade', 'Caonalyst', 'snellejelte', 'Guy_Broman', 'ReiAstra', 'flem_sy', 'JBF3', 'KolegaPolakYT', 'Pieface1091'] #"All division directorate of The Nighthawk Imperium. 
#> Currently LucarneHaven, rockstarmari, uhmrhino, Caonalyst, snellejelte, Guy_Broman, ReiAstra, flem_sy, JBF3, KolegaPolakYT, and Pieface1091."
phantom_spectre_targets = ["RisenVezyr"]

perm_spectre_groups = {
    "Nighthawk Combat Engineers: Leviathan": 33391710, #"Any and all members of Leviathans."
    "Nighthawk Imperial Peacekeeper Corps": 4543661 #"Imperial Peacekeeper Corps members."
}

phantom_spectre_groups = {
    "Nighthawk Manticore": 15026315
}

perm_spectre_roles = {
    4486074: [ #"Cerberus Drill Sergeant or higher"
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
    15026315: [ #"All Operatives of the Military Police Manticore."
        "Probationary Member",
        "Cadet",
        "Agent",
        "Operative",
        "Senior Operative",
        "Elite",
        "Auxilior",
        "Zealot",
        "Kaidon",
        "-",
        "Chief Superintendent",
        "Arbiter",
        "Deputy Chief",
        "Chief",
        "Administration",
        "Viceroy"
    ],
    1174414: [ #"TNI Commodore & TNI Admiralty."
        "| C | Commodore",
        "| HC | Admiral",
        "| HC | Arch Admiral",
        "| X | Supreme Admiral",
        "| X | Commander",
        "| X | Viceroy"
    ],
    3497000: [ #"Royal Guard Royal Officers."
        "Royal Officer"
    ],
    4809530: [ #"TNI Division High Command within...CE Ordinatus..."
        "| HC | Ordinatus",
        "| HC | Praefectus",
        "| X | Fabricator-General",
        "| X | Overseer",
        "| X | Administration",
        "| X | Viceroy"
    ],
    3496996: [ #"TNI Division High Command within...CO Commandant..."
        "Commandant",
        "Advisor",
        "Deputy Director",
        "Director",
        "Overseer",
        "Administration",
        "Commander",
        "Viceroy"
    ],
    3497030: [ #"#"TNI Division High Command within...MP CSI...""
        "| HC | Chief Superintendent",
        "| HC | Deputy Chief",
        "| C | Chief",
        "| X | Overseer",
        "| X | Commander",
        "| X | Administration",
        "| X | Viceroy"
    ],
    4734688: [ #"TNI Division High Command within...NRB Arbiters..."
        "Arbiter",
        "Warden",
        "Director",
        "Overseer",
        "Commander",
        "Administration",
        "Viceroy"
    ],
    3612873: [ #"TNI Division High Command within...VG Councils..."
        "C | Council",
        "C | Consul",
        "Forerunner",
        "Overseer",
        "Administration",
        "Commander",
        "Viceroy"
    ]
}

phantom_spectre_roles = {
}

perm_spectre_morphs = {
}

phantom_spectre_morphs = {
}

# RED CELL
bi_weekly_red_cell_targets = []

perm_red_cell_groups = {
    "Nighthawk Imperial Peacekeeper Corps": 4543661, #"Imperial Peacekeeper Corps members."
    "Nighthawk Manticore": 15026315, #"Any and all Manticore Operatives"
}

bi_weekly_red_cell_groups = {
}

#TODO BD "Supreme Command"
perm_red_cell_roles = {
    3497000: [ #"Royal Guard Officers"
        "Royal Officer"
    ],
    4486074: [ #Technically, Supreme Command is considered Captain-Major+, but I'm letting this slide because RC didn't know wtf it was either.
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
    4936035: [ #Confirmed via legomaster25182028 in Discord
        "Imperator",
        "Praefectus",
        "General",
        "Director",
        "Developer",
        "Overseer",
        "Administration",
        "Viceroy"
    ],
    4809530: [ #"Combat Engineers Officers" & "TNI/Div High Command"
        "| O | Moderatus",
        "| O | Dominatus",
        "| O | Magos",
        "| HC | Ordinatus",
        "| HC | Praefectus",
        "| X | Bot",
        "| X | Fabricator-General",
        "| X | Overseer",
        "| X | Administration",
        "| X | Viceroy"
    ],
    3497030: [ #"Military Police Officers" & "TNI/Div High Command"
        "| H | Inspector",
        "| H | Superintendent",
        "| HC | Chief Superintendent",
        "| HC | Deputy Chief",
        "| X | Developer",
        "| C | Chief",
        "| X | Overseer",
        "| X | Commander",
        "| X | Administration",
        "| X | Viceroy"
    ],
        1174414: [ #"TNI/Div High Command"
        "| C | Commodore",
        "| HC | Admiral",
        "| HC | Arch Admiral",
        "| X | Supreme Admiral",
        "| X | Commander",
        "| X | Viceroy"
    ],
    3496996: [ #"TNI/Div High Command"
        "Commandant",
        "Advisor",
        "Deputy Director",
        "Director",
        "Overseer",
        "Administration",
        "Commander",
        "Viceroy"
    ],
    4734688: [ #"TNI/Div High Command"
        "Arbiter",
        "Warden",
        "Director",
        "Overseer",
        "Commander",
        "Administration",
        "Viceroy"
    ],
    3612873: [ #"TNI/Div High Command"
        "C | Council",
        "C | Consul",
        "Forerunner",
        "Overseer",
        "Administration",
        "Commander",
        "Viceroy"
    ],
}

bi_weekly_red_cell_roles = {
    3497000: [ #"Weekly Operation: "Spears for me, you, and him?":"
        "Trial",
        "Knight",
        "Vindicator",
        "Sentinel",
        "Champion",
        "Royal Officer",
        "High Command",
        "Director",
        "Overseer",
        "Administration",
        "Commander",
        "Viceroy"
    ],
    1174414: [ #"Weekly Operation: "Spears for me, you, and him?":"
        "| HC | Admiral",
        "| HC | Arch Admiral",
        "| X | Supreme Admiral",
        "| X | Commander",
        "| X | Viceroy"
    ],
}

red_cell_morphs = {
}

# CHIMERA
weekly_chimera_targets = ["lam919", "DeadlyCraytos", "Rostrer", "bruhther789", "ReiAstra"] #"Individual hits...HIGH VALUE TARGET...ReiAstra"

weekly_chimera_groups = {
}

weekly_chimera_roles = {
    1174414: [ #HIGH VALUE TARGET...Admiral --> I know it says "admiral" specifically, but im giving myself leeway on this one
        "| HC | Admiral",
        "| HC | Arch Admiral",
        "| X | Supreme Admiral",
        "| X | Commander",
        "| X | Viceroy"
    ]
}

chimera_morphs = {
    "Nighthawk Military Police: Cerberus": 4486074, #Morph extermination...
    "Nighthawk Commandos": 3496996 #Morph extermination...
}

def search_users(session, keyword, use_countdown):
    print("-" * 40)
    url = f"https://users.roblox.com/v1/users/search?keyword={keyword}&limit=100"
    response = make_request(session, url)

    if response:
        data = response.json()
        users = data.get('data', [])
        found_user = False

        #we need to find out of our data which user is equal to our user of interest
        for user in users:
            if user['name'].lower() == keyword.lower():
                found_user = True
                print(f"Username: {user['name']}, DisplayName: {user['displayName']}, Id: {user['id']}")
                print("-" * 40)
                
                fetch_user_groups(session, user['id'], user['name'], use_countdown)
                break

        if not found_user:
            print(f"No exact match found for username: {keyword}")
    else:
        print(f"Failed to retrieve users.")

def fetch_user_groups(session, user_id, username, use_countdown):
    url = f"https://groups.roblox.com/v1/users/{user_id}/groups/roles"
    response = make_request(session, url)

    spectre_output = []
    red_cell_output = []
    chimera_output = []

    spectre_found = False
    red_cell_found = False
    chimera_found = False

    if response:
        data = response.json()
        groups = data.get('data', [])

        in_nighthawk_imperium = False

        #spec user check
        if username.lower() in [u.lower() for u in perm_spectre_targets]:
            spectre_output.append(f"{username} | Permanent Hit")
            spectre_found = True

        if username.lower() in [u.lower() for u in phantom_spectre_targets]:
            spectre_output.append(f"{username} | Phantom Assigned")
            spectre_found = True

        #NOTE: Only spectres need to differentiate perm hit and phantom assigned because the number of hits you need for each reward are different

        # red cell user check (only needed for bi since perm is group/group+role based)
        if username.lower() in [u.lower() for u in bi_weekly_red_cell_targets]:
            red_cell_output.append(f"{username}")
            red_cell_found = True

        # chimera user check
        if username.lower() in [u.lower() for u in weekly_chimera_targets]:
            chimera_output.append(f"{username}")
            chimera_found = True

        for group in groups:
            group_id = group['group']['id']
            group_name = group['group']['name']
            role_name = group['role']['name']

            #if they're not even in TNI, we know they're not a target. we could optimize this with a goto equivalent to avoid checking, but this program isn't intense.
            if group_id == 1174414:
                in_nighthawk_imperium = True

            #spec group check    
            if group_id in perm_spectre_groups.values():
                spectre_output.append(f"{group_name}, {username} | Permanent Hit")
                spectre_found = True

            if group_id in phantom_spectre_groups.values():
                spectre_output.append(f"{group_name}, {username} | Phantom Assigned")
                spectre_found = True

            #red cell groups check
            if group_id in perm_red_cell_groups.values():
                red_cell_output.append(f"{group_name}, {username}")
                red_cell_found = True

            if group_id in bi_weekly_red_cell_groups.values():
                red_cell_output.append(f"{group_name}, {username}")
                red_cell_found = True

            # chimera groups check
            if group_id in weekly_chimera_groups.values():
                chimera_output.append(f"{group_name}, {username}")
                chimera_found = True

            # spectre group + role check
            if group_id in perm_spectre_roles and role_name in perm_spectre_roles[group_id]:
                spectre_output.append(f"{group_name}, {role_name}, {username} | Permanent Hit")
                spectre_found = True

            if group_id in phantom_spectre_roles and role_name in phantom_spectre_roles[group_id]:
                spectre_output.append(f"{group_name}, {role_name}, {username} | Phantom Assigned")
                spectre_found = True

            # red cell group + role check
            if group_id in perm_red_cell_roles and role_name in perm_red_cell_roles[group_id]:
                red_cell_output.append(f"{group_name}, {role_name}, {username}")
                red_cell_found = True

            if group_id in bi_weekly_red_cell_roles and role_name in bi_weekly_red_cell_roles[group_id]:
                red_cell_output.append(f"{group_name}, {role_name}, {username}")
                red_cell_found = True

            # chimera group + role check
            if group_id in weekly_chimera_roles and role_name in weekly_chimera_roles[group_id]:
                chimera_output.append(f"{group_name}, {role_name}, {username}")
                chimera_found = True

            # some chimera and red cell targets can only be redeemed if they're in morph
            if group_id in red_cell_morphs.values():
                red_cell_output.append(f"{group_name}, {username} | MUST BE IN MORPH!")
                red_cell_found = True

            if group_id in chimera_morphs.values():
                chimera_output.append(f"{group_name}, {username} | MUST BE IN MORPH!")
                chimera_found = True

            if group_id in perm_spectre_morphs.values():
                spectre_output.append(f"{group_name}, {username} | MUST BE IN MORPH!")
                spectre_found = True

            if group_id in phantom_spectre_morphs.values():
                spectre_output.append(f"{group_name}, {username} | MUST BE IN MORPH!")
                spectre_found = True

        if not in_nighthawk_imperium:
            print(f"{username} is not in The Nighthawk Imperium. Not a target. Are you sure you typed the name in correctly?")

        if not spectre_found:
            spectre_output.append("XXXXXXXXXX")
        if not red_cell_found:
            red_cell_output.append("XXXXXXXXXX")
        if not chimera_found:
            chimera_output.append("XXXXXXXXXX")

        print("SPECTRES")
        for item in spectre_output:
            print(item)

        print("\nRED CELL")
        for item in red_cell_output:
            print(item)

        print("\nCHIMERA")
        for item in chimera_output:
            print(item)
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

def clear_terminal():
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

if __name__ == "__main__":
    session = requests.Session()
    print("=" * 40)
    cookie = input("Enter .ROBLOSECURITY cookie (or leave blank to skip): ")
    print("=" * 40)
    use_countdown = not cookie
    if cookie:
        session.headers.update({'Cookie': f'.ROBLOSECURITY={cookie}'})
        clear_terminal()#hide cookie
        print("=" * 40)

    while True:
        search_term = input("Enter user: ")
        search_users(session, search_term, use_countdown)
        print("=" * 40)