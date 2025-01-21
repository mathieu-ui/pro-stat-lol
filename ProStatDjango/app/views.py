import requests
from django.shortcuts import render
from django.http import JsonResponse
import app.scripts as lol

def index(request):
    return render(request, 'app/index.html')

def error(request):
    error = request.POST['error']
    return render(request, 'app/error.html', context={'error': error})

def masteries(request):
    if 'id' in request.POST:
        id = request.POST['id']
        tag = request.POST['tag']
    else:
        error = "Vous n'avez rien à faire là !"
        emote = "bee.webp"
        return render(request, 'app/error.html', context={'error': error,'emote': emote})
    riotid = f"{id}#{tag}"
    output = lol.get_puuid_by_riot_id(id,tag)

    if output == None:
        error = "Le Riot ID ne semble pas exister."
        emote = "blitz.webp"
        return render(request, template_name='app/error.html', context={'error':error,'emote': emote})
    elif output == "token":
        error = "Le token a expiré !"
        emote = "teemo.webp"
        return render(request, template_name='app/error.html', context={'error':error,'emote': emote})

    all_champs = lol.get_all_champs_infos(output)
    big_list = []
    for c in all_champs:
        lil_list = []

        data = lol.trouver_nom_par_id(int(c["championId"]))
        lil_list.append(data[0])
        lil_list.append(c["championPoints"])
        lil_list.append(data[1])
        big_list.append(lil_list.copy())
        lil_list.clear()

    return render(request, 'app/querout.html', context={'output':output, 'all_champs':big_list, 'riotid':riotid})