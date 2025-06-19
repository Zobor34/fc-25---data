import requests

class FutApiClient:
   def get_players(self, limit=50):
    url = f"https://www.futbin.org/api/players?platform={self.platform}&limit={limit}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data if isinstance(data, list) else data.get("players", [])
    else:
        print(f"❌ Erreur API FUTBIN: {response.status_code}")
        return []

