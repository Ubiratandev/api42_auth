import requests
from django.conf import settings

def fetch_cursus(acces_token):
    url = f"{settings.API_BASE_URL}/cursus"

    headers = {"Authorization": f"Bearer {acces_token}"}
    try:
        response = requests.get(url, headers=headers)
        print("Response status:", response.status_code)  # Exibe o status code da resposta
        print("Response content:", response.text)  
        print("token:",acces_token)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Erro ao buscar cursus:{response.status_code}"
             )
    except requests.exceptions.RequestException as e:
        print(f"erro {e}")
        raise
    