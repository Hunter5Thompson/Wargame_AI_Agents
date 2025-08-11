from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict, Literal

class TacticalState(TypedDict):
    """Taktischer Zustand für US Airmobile Doktrin"""
    enemy_contact: bool
    enemy_strength: str  # "squad", "platoon", "company", "battalion"
    terrain: str  # "open", "jungle", "urban", "mountain"
    air_support_available: bool
    artillery_available: bool
    casualties: float
    ammunition: float
    decision: str
    confidence: float

def create_us_airmobile_doctrine() -> StateGraph:
    """US Airmobile Doktrin als LangGraph"""

    graph = StateGraph(TacticalState)

    # Knoten definieren
    graph.add_node("assess_contact", assess_enemy_contact)
    graph.add_node("call_for_fire", request_fire_support)
    graph.add_node("air_assault", execute_air_assault)
    graph.add_node("defensive_perimeter", establish_perimeter)
    graph.add_node("tactical_withdrawal", conduct_withdrawal)
    graph.add_node("pursuit", pursue_enemy)
    graph.add_node("medevac", request_medevac)

    # Entscheidungslogik
    def routing_logic(state: TacticalState) -> str:
        """Doktrin-basierte Routing-Entscheidung"""

        # Kritische Verluste -> Rückzug
        if state["casualties"] > 40:
            return "medevac"

        # Feindkontakt Entscheidungsbaum
        if state["enemy_contact"]:
            # Übermacht -> Feuerunterstützung
            if state["enemy_strength"] in ["company", "battalion"]:
                if state["artillery_available"] or state["air_support_available"]:
                    return "call_for_fire"
                else:
                    return "defensive_perimeter"

            # Gleichwertig/Unterlegen -> Angriff
            elif state["enemy_strength"] in ["squad", "platoon"]:
                if state["terrain"] == "open" and state["air_support_available"]:
                    return "air_assault"
                else:
                    return "pursuit"

        # Kein Kontakt -> Defensive
        return "defensive_perimeter"

    # Kanten basierend auf Doktrin
    graph.add_conditional_edges(
        "assess_contact",
        routing_logic,
        {
            "call_for_fire": "call_for_fire",
            "air_assault": "air_assault",
            "defensive_perimeter": "defensive_perimeter",
            "tactical_withdrawal": "tactical_withdrawal",
            "pursuit": "pursuit",
            "medevac": "medevac"
        }
    )

    # Weitere Übergänge
    graph.add_edge("call_for_fire", "assess_contact")
    graph.add_edge("air_assault", END)
    graph.add_edge("medevac", "tactical_withdrawal")
    graph.add_edge("tactical_withdrawal", END)

    return graph.compile()

# Verwendung
async def execute_doctrine(situation: Dict) -> Dict:
    """Führe Doktrin-basierte Entscheidung aus"""

    doctrine = create_us_airmobile_doctrine()

    initial_state = TacticalState(
        enemy_contact=situation.get("enemy_contact", False),
        enemy_strength=situation.get("enemy_strength", "unknown"),
        terrain=situation.get("terrain", "jungle"),
        air_support_available=situation.get("air_available", True),
        artillery_available=situation.get("arty_available", True),
        casualties=situation.get("casualties", 0),
        ammunition=situation.get("ammo", 100),
        decision="",
        confidence=0.0
    )

    result = await doctrine.ainvoke(initial_state)
    return result
