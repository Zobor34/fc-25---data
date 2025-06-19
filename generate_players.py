import requests
import json

URL = "https://raw.githubusercontent.com/futdb/data/main/players.json"

def fetch_players():
    r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    if r.status_code == 200:
        return r.json()  # la liste complète des joueurs
    print("Erreur HTTP :", r.status_code)
    return []

if __name__ == "__main__":
    players = fetch_players()
    print(f"Nombre de joueurs récupérés : {len(players)}")
    with open("players.json", "w", encoding="utf-8") as f:
        json.dump(players, f, indent=2, ensure_ascii=False)
