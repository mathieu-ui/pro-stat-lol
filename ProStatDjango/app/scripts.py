import requests
from urllib.parse import quote

API_KEY = "RGAPI-7b58915b-e604-45ba-9237-068907d5a245"

def get_puuid_by_riot_id(name, tag):
    BASE_URL = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id"
    encoded_name = quote(name)
    encoded_tag = quote(tag)
    url = f"{BASE_URL}/{encoded_name}/{encoded_tag}"

    # Prépare les en-têtes avec la clé API
    headers = {"X-Riot-Token": API_KEY}

    # Effectue la requête
    response = requests.get(url, headers=headers)

    # Gère la réponse
    if response.status_code == 200:
        a = response.json()
        print("PUUID OK")
        return a["puuid"]
    else:
        print(f"Erreur {response.status_code}: {response.text}")
        return None

def get_champ_infos(puuid,champ_id):
    url = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champ_id}?api_key={API_KEY}"
    response = requests.get(url)
    print("Get Champ OK")
    return response.json()

def get_all_champs_infos(puuid):
    url = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}?api_key={API_KEY}"
    response = requests.get(url)
    print("All champs OK")
    return response.json()


def trouver_nom_par_id(id_recherche):
    import csv
    csv_path = "app/champions.csv"
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['key'] == str(id_recherche):
                return row['name']
    return f"ID {id_recherche}"


"""riot_name = "Mr Bark"  # Nom du joueur
riot_tag = "turbo"  # Tag du joueur
account_info = get_puuid_by_riot_id(riot_name, riot_tag)

#print(account_info)
print(get_champ_infos(account_info, 42))
arabe = get_all_champs_infos(account_info)

for a in arabe:

    name = trouver_nom_par_id("champions.csv",int(a["championId"]))
    print(f"{a["championId"]},{name}")"""