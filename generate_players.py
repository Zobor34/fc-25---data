import json
from futapi.fut_api import FutApiClient

client = FutApiClient(platform="ps")  # ou "xbox" ou "pc"

# Exemple : récupérer les 50 premiers joueurs FUT
players = client.get_players(limit=50)

formatted_players = []

for p in players:
    formatted_players.append({
        "id": p["id"],
        "name": p["name"],
        "overall": p["rating"],
        "position": p["position"],
        "club": p["club"]["name"] if p.get("club") else "N/A",
        "league": p["league"]["name"] if p.get("league") else "N/A",
        "nation": p["nation"]["name"] if p.get("nation") else "N/A",
        "version": p["version"] or "Standard"
    })

with open("players.json", "w", encoding="utf-8") as f:
    json.dump(formatted_players, f, indent=2, ensure_ascii=False)

print(f"✅ {len(formatted_players)} joueurs écrits dans players.json")
