import json
from datetime import datetime

# Exemple temporaire — à remplacer plus tard par une vraie API ou un fetch
players = [
    {
        "id": 1,
        "name": "Kylian Mbappé",
        "overall": 92,
        "position": "ST",
        "club": "PSG",
        "league": "Ligue 1",
        "nation": "France",
        "version": "TOTY"
    },
    {
        "id": 2,
        "name": "Jude Bellingham",
        "overall": 91,
        "position": "CM",
        "club": "Real Madrid",
        "league": "LaLiga",
        "nation": "England",
        "version": "TOTS"
    },
    {
        "id": 3,
        "name": "Cristiano Ronaldo",
        "overall": 90,
        "position": "ST",
        "club": "Al Nassr",
        "league": "MBS Pro League",
        "nation": "Portugal",
        "version": "Flashback"
    }
]

# Ajouter une date de mise à jour pour vérification
meta = {
    "updated_at": datetime.utcnow().isoformat() + "Z"
}

# Format final : liste de joueurs (tu peux inclure meta si tu veux)
with open("players.json", "w", encoding="utf-8") as f:
    json.dump(players, f, indent=2, ensure_ascii=False)

print("✅ players.json généré avec", len(players), "joueurs")
