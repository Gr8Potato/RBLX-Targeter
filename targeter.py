import requests

target_users = ["41uis", "Expiral"]

groups_of_interest = {
    "Cerberus": 4486074,
}

roles_of_interest = {
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
    ]
}

def search_users(keyword):
    url = f"https://users.roblox.com/v1/users/search?keyword={keyword}&limit=100"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        users = data.get('data', [])
        for user in users:
            if user['name'].lower() == keyword.lower():
                print(f"Username: {user['name']}, DisplayName: {user['displayName']}, Id: {user['id']}")
                is_target = False
                
                if user['name'].lower() in [u.lower() for u in target_users]:
                    print(f"Target User: {user['name']}")
                    is_target = True
                
                fetch_user_groups(user['id'], is_target)
                break
    else:
        print(f"Failed to retrieve users: {response.status_code}")

def fetch_user_groups(user_id, is_target):
    url = f"https://groups.roblox.com/v1/users/{user_id}/groups/roles"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        groups = data.get('data', [])
        for group in groups:
            group_id = group['group']['id']
            group_name = group['group']['name']
            role_name = group['role']['name']
            
            if group_id in groups_of_interest.values():
                print(f"User is in a target group: {group_name} (ID: {group_id})")
                is_target = True

            if group_id in roles_of_interest and role_name in roles_of_interest[group_id]:
                print(f"Target Role: {role_name} in Group: {group_name} (ID: {group_id})")
                is_target = True
        
        if not is_target:
            print(f"No target roles or groups of interest found for User ID {user_id}.")
    else:
        print(f"Failed to retrieve groups for User ID {user_id}: {response.status_code}")

if __name__ == "__main__":
    while True:
        search_term = input("Enter a keyword to search for users: ")
        search_users(search_term)