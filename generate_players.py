import json
from futapi.fut_api import FutApiClient

client = FutApiClient(platform="ps")  # "xbox", "pc" aussi dispo

# 🔁 Récupère les 30 premiers joueurs FUT
players = client.get_players(limit=30)

formatted_players = []

for p in players:
    formatted_players.append({
        "id": p.get("id", 0),
        "name": p.get("name", "Inconnu"),
        "overall": p.get("rating", 0),
        "position": p.get("position", "N/A"),
        "club": p.get("club", {}).get("name", "N/A"),
        "league": p.get("league", {}).get("name", "N/A"),
        "nation": p.get("nation", {}).get("name", "N/A"),
        "version": p.get("version", "Standard")
    })

with open("players.json", "w", encoding="utf-8") as f:
    json.dump(formatted_players, f, indent=2, ensure_ascii=False)

print(f"✅ {len(formatted_players)} joueurs écrits dans players.json")
