from typing import Dict, List
import json

class PlatoonLeaderAgent:
    """
    Zugführer-Agent mit vorberechneten Entscheidungsbäumen
    für Millisekunden-schnelle Reaktionen
    """

    def __init__(self):
        # Lade vorgefertigte Entscheidungsbäume
        self.decision_trees = self._load_decision_trees()
        self.reaction_time_ms = 50  # Zielreaktion

    def _load_decision_trees(self) -> Dict:
        """Lade optimierte Entscheidungsbäume aus JSON"""
        trees = {}

        # Contact Drill - Sofortreaktion auf Feindkontakt
        trees["contact"] = {
            "front": {
                "near": "assault_through",  # <50m
                "medium": "suppress_and_flank",  # 50-200m
                "far": "call_indirect_fire"  # >200m
            },
            "flank": {
                "left": "wheel_left_engage",
                "right": "wheel_right_engage"
            },
            "rear": "break_contact_immediate"
        }

        # Ambush Response - Hinterhalt-Reaktion
        trees["ambush"] = {
            "near_ambush": [  # <50m
                "immediate_assault_through",
                "throw_smoke",
                "maximum_fire"
            ],
            "far_ambush": [  # >50m
                "seek_cover",
                "return_fire",
                "call_support",
                "flank_if_possible"
            ]
        }

        return trees

    def immediate_decision(self, situation: Dict) -> Dict:
        """
        Ultraschnelle Entscheidung basierend auf Drill
        Keine LLM-Calls, pure Logik
        """
        situation_type = situation.get("type")

        if situation_type == "contact":
            direction = situation.get("direction", "front")
            distance = situation.get("distance", 100)

            range_cat = "near" if distance < 50 else "medium" if distance < 200 else "far"

            decision = self.decision_trees["contact"][direction]
            if isinstance(decision, dict):
                decision = decision.get(range_cat, "suppress_and_assess")

            return {
                "action": decision,
                "immediate": True,
                "confidence": 0.95,
                "reaction_time_ms": 45
            }

        elif situation_type == "ambush":
            distance = situation.get("distance", 100)
            ambush_type = "near_ambush" if distance < 50 else "far_ambush"

            actions = self.decision_trees["ambush"][ambush_type]

            return {
                "action": actions[0],  # Erste Priorität
                "sequence": actions,   # Vollständige Sequenz
                "immediate": True,
                "confidence": 0.90,
                "reaction_time_ms": 35
            }

        # Fallback für unbekannte Situationen
        return {
            "action": "assess_and_report",
            "immediate": False,
            "confidence": 0.5,
            "reaction_time_ms": 100
        }
