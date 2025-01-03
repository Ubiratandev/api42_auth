from django.shortcuts import render

import requests
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from .services import fetch_cursus

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TOKEN_URL = "https://api.intra.42.fr/oauth/token"

acces_token = None
def get_acces_token():
    global acces_token
    if acces_token is None:
        payload = {
         "grant_type": "client_credentials",
         "client_id": CLIENT_ID,
         "client_secret": CLIENT_SECRET,
         }
        response = requests.post(TOKEN_URL, data=payload)
    
        # Verifica se a resposta foi bem-sucedida (status 200)
        if response.status_code == 200:
            acces_token = response.json().get("access_token")
        else:
        # Exceção em caso de erro com mais detalhes da resposta
            raise Exception(f"Erro ao obter token: {response.status_code} - {response.text}")
    return acces_token
    
def test_api(request):
    
    try:
        token = get_acces_token()
        return JsonResponse({'access_token':token})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status = 500)

def list_cursus(request):
    try:
        token = get_acces_token()
        # Busca a lista de cursus da API
        cursus_list = fetch_cursus(token)
        return render(request, "cursus_list.html", {"cursus_list": cursus_list})
    except Exception as e:
        return render(request, "error.html", {"error": str(e)})