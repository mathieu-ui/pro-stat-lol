import requests
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        response = requests.get(f'https://api.example.com/search?q={query}')
        data = response.json()
        return JsonResponse(data)
    return render(request, 'app/index.html')