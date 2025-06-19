import requests, json

URL = "https://raw.githubusercontent.com/futdb/data/main/players.json"  # ou tout autre test

def fetch_players():
    print("[INFO] Envoi de la requête...")
    r = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})

    print("[DEBUG] Status code:", r.status_code)
    print("[DEBUG] Contenu brut:", r.text[:200])  # On affiche juste les 200 premiers caractères

    if r.status_code == 200:
        try:
            return r.json()
        except Exception as e:
            print("[ERROR] JSON parse error:", str(e))
            return []
    else:
        print("[ERROR] HTTP", r.status_code)
        return []

if __name__ == "__main__":
    players = fetch_players()
    print("[INFO] Total joueurs récupérés :", len(players))
    with open("players.json", "w", encoding="utf-8") as f:
        json.dump(players, f, indent=2, ensure_ascii=False)
print("[DEBUG] JSON brut :", data)  # juste après r.json()
