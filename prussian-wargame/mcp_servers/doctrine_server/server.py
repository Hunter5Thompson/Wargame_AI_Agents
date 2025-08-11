from fastapi import FastAPI, WebSocket
from typing import Dict, List
import json
import asyncio

app = FastAPI()

class DoctrineMCPServer:
    """MCP Server für Doktrin-Daten und Entscheidungsbäume"""

    def __init__(self):
        self.decision_cache = {}
        self.historical_battles = self._load_historical_data()
        self.doctrine_patterns = self._load_doctrine_patterns()

    def _load_historical_data(self) -> List[Dict]:
        """Lade historische Schlachtdaten"""
        # Da Nang spezifische Gefechte
        return [
            {
                "date": "1966-01-28",
                "operation": "Operation Double Eagle",
                "units": ["1st Bn, 3rd Marines", "VC 325th Division"],
                "outcome": "tactical_victory",
                "lessons": [
                    "Combined arms essential in jungle",
                    "Artillery preparation before assault",
                    "Maintain unit cohesion"
                ]
            },
            {
                "date": "1966-03-04",
                "operation": "Operation Utah",
                "units": ["2/7 Marines", "ARVN 1st Div", "NVA 21st Regiment"],
                "outcome": "costly_victory",
                "lessons": [
                    "NVA will stand and fight when cornered",
                    "Coordination with ARVN critical",
                    "Medevac routes must be secured"
                ]
            }
            # Weitere historische Daten...
        ]

    async def get_tactical_precedent(self, situation: Dict) -> Dict:
        """Finde historische Präzedenzfälle für aktuelle Situation"""

        similar_battles = []
        for battle in self.historical_battles:
            similarity = self._calculate_similarity(situation, battle)
            if similarity > 0.7:
                similar_battles.append({
                    "battle": battle,
                    "similarity": similarity
                })

        # Sortiere nach Ähnlichkeit
        similar_battles.sort(key=lambda x: x["similarity"], reverse=True)

        if similar_battles:
            best_match = similar_battles[0]["battle"]
            return {
                "precedent": best_match,
                "recommended_actions": best_match["lessons"],
                "confidence": similar_battles[0]["similarity"]
            }

        return {"precedent": None, "recommended_actions": [], "confidence": 0.0}

    @app.websocket("/ws/doctrine")
    async def doctrine_websocket(self, websocket: WebSocket):
        """WebSocket für Echtzeit-Doktrin-Updates"""
        await websocket.accept()

        try:
            while True:
                # Empfange Anfrage
                data = await websocket.receive_json()

                # Verarbeite basierend auf Typ
                if data["type"] == "tactical_query":
                    response = await self.get_tactical_precedent(data["situation"])
                elif data["type"] == "immediate_decision":
                    response = self.get_immediate_response(data["situation"])
                else:
                    response = {"error": "Unknown query type"}

                # Sende Antwort
                await websocket.send_json(response)

        except Exception as e:
            print(f"WebSocket error: {e}")
            await websocket.close()

# Server starten
mcp_server = DoctrineMCPServer()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
