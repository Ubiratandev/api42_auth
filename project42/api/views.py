from django.shortcuts import render
import json
import requests
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from .services import fetch_cursus
from .services import fetch_login_stats
from datetime import datetime, timedelta
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
def  list_status(request):
    try:
        token = get_acces_token()
        end_date= datetime.now()
        start_date = end_date - timedelta(days=90)
        start_date_str = start_date.strftime("%Y-%m-%dT%H:%M:%S")
        end_date_str = end_date.strftime("%Y-%m-%dT%H:%M:%S")
        raw_status_list = fetch_login_stats(token, begin_at=start_date_str, end_at= end_date_str)
        print(f"raw list:{raw_status_list}")
        if not isinstance(raw_status_list, dict):
           raise ValueError("o retorno nao é um dicionario") 
        total_hours = 0
        for hours in raw_status_list.values():
            time_parts = hours.split(":")
            total_hours += int(time_parts[0])
        status_list = raw_status_list
        print(f"status list :",status_list)
        return render(request, "login_status.html", {"status_list":status_list, "total_hours":total_hours})
    except Exception as e:
        return render(request, "error.html",{"error":str(e)})