import requests
from urllib.parse import quote
import os, json

JSON_PATH = f"app/config.json"

def get_token():
    with open(JSON_PATH, 'r') as fichier:
        data = json.load(fichier)
    return data.get('token')

def replace_token(new_token):
    with open(JSON_PATH, 'r') as fichier:
        data = json.load(fichier)

    # Modifier la valeur de "token"
    data['token'] = new_token

    # Écrire les modifications dans le fichier JSON
    with open(JSON_PATH, 'w') as fichier:
        json.dump(data, fichier, indent=4)


def get_puuid_by_riot_id(name, tag):
    BASE_URL = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id"
    encoded_name = quote(name)
    encoded_tag = quote(tag)
    url = f"{BASE_URL}/{encoded_name}/{encoded_tag}"

    # Prépare les en-têtes avec la clé API
    headers = {"X-Riot-Token": get_token()}

    # Effectue la requête
    response = requests.get(url, headers=headers)

    # Gère la réponse
    if response.status_code == 200:
        a = response.json()
        print("PUUID OK")
        return a["puuid"]
    elif response.status_code == 403:
        return "token"
    else:
        print(f"Erreur {response.status_code}: {response.text}")
        return None

def get_champ_infos(puuid,champ_id):
    url = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/by-champion/{champ_id}?api_key={get_token()}"
    response = requests.get(url)
    print("Get Champ OK")
    return response.json()

def get_all_champs_infos(puuid):
    url = f"https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}?api_key={get_token()}"
    response = requests.get(url)
    print("All champs OK")
    return response.json()

def get_riotid_from_puuid(puuid):
    # gameName, tagLine
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}?api_key={get_token()}"
    response = requests.get(url)

    try:
        name = response.json()["gameName"]+"#"+response.json()["tagLine"]
    except:
        name = "error name"
    return name

def trouver_nom_par_id(id_recherche):

    return_list = []
    import csv
    csv_path = f"app/champions.csv"
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['key'] == str(id_recherche):
                return_list.append(row['name'])
                break
    files = []
    for fichier in os.listdir(f"app/static/loading"):
        if row['name'] in fichier:  # Vérification si la chaîne est dans le nom du fichier
            files.append(f"static/loading/{fichier}")
    if len(files) == 0:
        files.append("static/loading/Teemo.jpg")
    return_list.append(files[0])
    return return_list

def get_last_10_matches(puuid):
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?api_key={get_token()}"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        print("Matches retrieved successfully")
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []

def get_match_info(match_id):
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={get_token()}"
    response = requests.get(url)

    return response.json()

def match_to_json(match_id):
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={get_token()}"
    response = requests.get(url)
    match_data = response.json()
    with open(f"app/static/game.json", "w") as file:
        json.dump(match_data, file, indent=4)