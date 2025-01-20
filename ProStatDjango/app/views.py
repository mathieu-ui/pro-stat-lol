import requests
from django.shortcuts import render
from django.http import JsonResponse
import app.scripts as lol

def index(request):
    return render(request, 'app/index.html')

def out(request):
    id = request.POST['id']
    tag = request.POST['tag']
    riotid = f"{id}#{tag}"
    output = lol.get_puuid_by_riot_id(id,tag)

    if output == None:
        error = "Le Riot ID ne semble pas exister."
        return render(request, template_name='app/index.html', context={'error':error})

    all_champs = lol.get_all_champs_infos(output)
    big_list = []
    for c in all_champs:
        lil_list = []
        name = lol.trouver_nom_par_id(int(c["championId"]))
        print(f"{c["championId"]},{name}")
        lil_list.append(name)
        lil_list.append(c["championPoints"])
        big_list.append(lil_list.copy())
        lil_list.clear()

    return render(request, 'app/querout.html', context={'output':output, 'all_champs':big_list, 'riotid':riotid})