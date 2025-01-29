import requests
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
import app.scripts as lol
from datetime import datetime, timezone, timedelta
import json

import platform

if platform.system() == "Windows":
    BASE_PATH = "ProStatDjango/"
else:
    BASE_PATH = ""

JSON_PATH = f"{BASE_PATH}config.json"
def index(request):

    query = lol.get_puuid_by_riot_id("Mr Bark", "turbo")
    print(lol.get_puuid_by_riot_id("Mr Bark", "turbo"))
    if query == None or query == 'token':
        token_up = 0
    else:
        token_up = 1

    return render(request, 'app/index.html', context={'token_up':token_up})

def error(request):
    error = request.POST['error']
    return render(request, 'app/error.html', context={'error': error})

def match_overview(request, game_code):
    # Charger les données du match en JSON
    lol.match_to_json(game_code)  # Appel de votre fonction pour générer le fichier JSON
    file_path = f"{BASE_PATH}app/static/game.json"  # Chemin vers votre fichier
    with open(file_path, "r") as file:
        data = json.load(file)

    # Conversion de la durée de la partie en minutes et secondes
    timestamp = data["info"]["gameDuration"]
    datetime_str = f"{round(timestamp / 60)}m {timestamp % 60}s"

    # Informations générales
    general_info = {
        "mode_de_jeu": data["info"]["gameMode"],
        "duree_partie": datetime_str,
        "carte": data["info"]["mapId"]
    }

    # Organiser les joueurs par équipe
    team_1 = []
    team_2 = []

    for participant in data["info"]["participants"]:
        player = {
            "nom_invocateur": participant.get("summonerName", "Anonyme"),
            "position": participant.get("teamPosition", "Non spécifié"),
            "niveau_atteint": participant["champLevel"],
            "kda": f"{participant['kills']} / {participant['deaths']} / {participant['assists']}",
            "gold_gagne": participant["goldEarned"],
            "degats_champions": participant["totalDamageDealtToChampions"],
            "vision_score": participant["visionScore"],
            "items": [participant.get(f"item{i}") for i in range(6)]
        }

        if participant["teamId"] == 100:
            team_1.append(player)
        elif participant["teamId"] == 200:
            team_2.append(player)

    # Déterminer l'équipe gagnante (par exemple en fonction du `teamId` gagnant)
    # Supposons que vous ayez une méthode pour récupérer cela, ou utilisez un critère comme `winningTeamId`
    winning_team_id = data["info"].get("winningTeam", 100)  # Exemple de critère

    # Préparer le contexte pour la page HTML
    context = {
        "general_info": general_info,
        "team_1": team_1,
        "team_2": team_2,
        "game_winner": 1 if winning_team_id == 100 else 2  # Définir l'équipe gagnante
    }

    return render(request, "app/game_info.html", context)

def redirector(request):
    destination = request.POST.get("action")

    if destination == "masteries":

        if 'id' in request.POST:
            id = request.POST['id']
            tag = request.POST['tag']
        else:
            error = "Vous n'avez rien à faire là !"
            emote = "bee.webp"
            return render(request, 'app/error.html', context={'error': error, 'emote': emote})

        riotid = f"{id}#{tag}"
        output = lol.get_puuid_by_riot_id(id, tag)

        if output == None:
            error = "Le Riot ID ne semble pas exister."
            emote = "blitz.webp"
            return render(request, template_name='app/error.html', context={'error': error, 'emote': emote})
        elif output == "token":
            error = "Le token a expiré !"
            emote = "teemo.webp"
            return render(request, template_name='app/error.html', context={'error': error, 'emote': emote})

        all_champs = lol.get_all_champs_infos(output)
        big_list = []
        for c in all_champs:
            lil_list = []

            data = lol.trouver_nom_par_id(int(c["championId"]))
            print(data)
            lil_list.append(data[0])
            lil_list.append(c["championPoints"])
            lil_list.append(data[1])
            big_list.append(lil_list.copy())
            lil_list.clear()

        return render(request, 'app/querout.html', context={'output': output, 'all_champs': big_list, 'riotid': riotid, 'verif_flag':"OK"})

    elif destination == "matchs":

        if request.method == "POST":
            riot_name = request.POST.get("id")
            riot_tag = request.POST.get("tag")
            puuid = lol.get_puuid_by_riot_id(riot_name, riot_tag)
            if puuid == None:
                puuid = "bober"
            if len(puuid) > 10:
                matches = lol.get_last_10_matches(puuid)[:15]

                matches_info = []

                for match in matches:
                    match_info = []
                    lol.match_to_json(match)

                    file_path = JSON_PATH  # Chemin vers votre fichier
                    with open(f"{BASE_PATH}app/static/game.json", "r") as file:
                        data = json.load(file)

                    timestamp_s = data.get("info").get("gameStartTimestamp") / 1000
                    date_time = datetime.fromtimestamp(timestamp_s, tz=timezone.utc)
                    formatted_date_time = date_time.strftime("%d-%m-%Y à %H:%M")

                    match_info.append(match)
                    match_info.append(formatted_date_time)
                    match_info.append(data.get("info").get("gameMode"))
                    match_info.append(f"{round(data.get("info").get("gameDuration")/60)}m {data.get("info").get("gameDuration")%60}s")

                    matches_info.append(match_info.copy())
                    match_info.clear()



                return render(request, 'app/match.html', {'riotid': riot_name, 'matches': matches_info, 'verif_flag':"OK"})
            elif puuid == "token":
                error = "Le token a expiré !"
                emote = "teemo.webp"
                return render(request, template_name='app/error.html', context={'error': error, 'emote': emote})
            else:
                error = "Le Riot ID ne semble pas exister."
                emote = "blitz.webp"
                return render(request, template_name='app/error.html', context={'error': error, 'emote': emote})
        return render(request, 'app/index.html')
    else :
        return redirect('index')


def add_token(request):
    if 'token' in request.POST:
        TOKEN = request.POST.get("token")
        lol.replace_token(TOKEN)

    query = lol.get_puuid_by_riot_id("Mr Bark","turbo")

    if query == None or query == 'token':
        error = "Le token fourni n'est pas correct ! "
        emote = "blitz.webp"
        return render(request, template_name='app/error.html', context={'error': error, 'emote': emote})
    else:
        error = "Le token fourni fonctionne correctement !"
        emote = "lux.webp"
        return render(request, template_name='app/error.html', context={'error': error, 'emote': emote})
