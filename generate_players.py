import requests, json

URL = "https://www.easports.com/fifa/ultimate-team/web-app/content/B1BA185F-01234567-89AB-CDEF-1234567890AB/2025/fut/items/web/players_meta.json"

def fetch_players():
    r = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
    if r.status_code == 200:
        data = r.json()
        players = data.get("Items", [])  # les joueurs se trouvent dans "Items"
        print(f"[INFO] Joueurs récupérés :", len(players))
        return players
    print("[ERROR] HTTP", r.status_code)
    return []

if __name__ == "__main__":
    players = fetch_players()
    with open("players.json", "w", encoding="utf-8") as f:
        json.dump(players, f, indent=2, ensure_ascii=False)
