import requests
from django.conf import settings

def fetch_cursus(acces_token):
    url = f"{settings.API_BASE_URL}/cursus"
    headers = {"Authorization": f"Bearer {acces_token}"}
    try:
        response = requests.get(url, headers=headers)
        print(f"acces_token:{acces_token}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Erro ao buscar cursus:{response.status_code}"
             )
    except requests.exceptions.RequestException as e:
        print(f"erro {e}")
        raise
def fetch_login_stats(acces_token, begin_at=None, end_at=None, time_zone=None):
    id = 188072
    url = f"{settings.API_BASE_URL}/users/{id}/locations_stats"
    headers = {"Authorization" : f"Bearer {acces_token}"}
    params={}
    if begin_at:
        params['begin_at']= begin_at
    if end_at:
        params['ent_at']=end_at
    if time_zone:
        params['time_zone']= time_zone
    try:
        response = requests.get(url, headers= headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"error:{response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"erro:{e}")
        raise
    