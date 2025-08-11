# Wargame_AI_Agents
A new approach to the old Prussian war game. SLM, Langgraph and MCP Server are to represent the PoC.
prussian-wargame/
├── docker-compose.yml              # Container-Orchestrierung
├── requirements.txt                # Python Dependencies
├── .env                           # Umgebungsvariablen
│
├── core/                          # Kern-Framework
│   ├── __init__.py
│   ├── domain/                   # Domain Models
│   │   ├── units.py             # Einheitendefinitionen
│   │   ├── terrain.py           # Geländemodelle
│   │   ├── orders.py            # Befehlsstrukturen
│   │   └── combat.py            # Kampfmechaniken
│   │
│   ├── simulation/               # Simulationskern
│   │   ├── engine.py            # Hauptsimulation
│   │   ├── physics.py           # Ballistik & Bewegung
│   │   ├── visibility.py        # Line-of-Sight
│   │   └── weather.py           # Wettereffekte
│   │
│   └── analytics/                # Analyse & Metriken
│       ├── lanchester.py        # Kampfmodelle
│       ├── logistics.py         # Versorgungsmodelle
│       └── morale.py            # Moralberechnungen
│
├── agents/                        # KI-Agenten (LangGraph)
│   ├── __init__.py
│   ├── doctrines/                # Militärdoktrinen
│   │   ├── us_airmobile.py      # US Air Cavalry Doktrin
│   │   ├── nva_peoples_war.py   # NVA Volkskrieg
│   │   ├── arvn_defensive.py    # ARVN Defensive
│   │   └── vc_guerrilla.py      # VC Guerilla Taktiken
│   │
│   ├── commanders/               # Kommandoebenen
│   │   ├── strategic.py         # Division/Corps
│   │   ├── operational.py       # Brigade/Regiment
│   │   └── tactical.py          # Battalion/Company
│   │
│   ├── specialists/              # Spezialisierte Agenten
│   │   ├── platoon_leader.py    # Zugführer (Schnelle Taktik)
│   │   ├── fire_support.py      # Artillerie-Koordinator
│   │   ├── intel_analyst.py     # S2 Intelligence
│   │   └── logistics_officer.py # S4 Versorgung
│   │
│   └── graphs/                   # LangGraph Definitionen
│       ├── command_graph.py     # Befehlskette
│       ├── ooda_loop.py         # OODA Decision Cycle
│       └── combat_flow.py       # Gefechtsablauf
│
├── mcp_servers/                   # MCP Server Integration
│   ├── __init__.py
│   ├── historical_data/          # Historische Daten Server
│   │   ├── vietnam_battles.py   # Schlacht-Datenbank
│   │   ├── unit_histories.py    # Einheiten-Historie
│   │   └── terrain_maps.py      # Geländekarten
│   │
│   ├── doctrine_server/          # Doktrin-Server
│   │   ├── server.py            # MCP Server Implementation
│   │   ├── decision_trees/      # Vorgefertigte Entscheidungen
│   │   │   ├── contact_drill.json
│   │   │   ├── ambush_response.json
│   │   │   └── medevac_procedure.json
│   │   └── knowledge_base.db    # Taktik-Datenbank
│   │
│   └── realtime_server/          # Echtzeit-Daten
│       ├── weather_service.py   # Wetter-Updates
│       └── intel_feed.py        # Intelligence Updates
│
├── models/                        # LLM Modelle
│   ├── configs/
│   │   ├── ollama_config.yml    # Ollama Einstellungen
│   │   ├── model_routing.yml    # Model-Routing Rules
│   │   └── quantization.yml     # Quantisierungs-Settings
│   │
│   └── prompts/                  # System Prompts
│       ├── platoon_leader.md    # Zugführer Prompt
│       ├── battalion_co.md      # Bataillonskommandeur
│       └── intel_analyst.md     # Nachrichtenoffizier
│
├── scenarios/                     # Szenario-Definitionen
│   ├── da_nang_1966/
│   │   ├── scenario.json        # Szenario-Parameter
│   │   ├── orbat_us.json        # US Order of Battle
│   │   ├── orbat_nva_vc.json    # NVA/VC Forces
│   │   ├── terrain.geojson      # Geländedaten
│   │   └── objectives.json      # Missionsziele
│   │
│   └── templates/                # Szenario-Templates
│       ├── meeting_engagement.json
│       ├── defense.json
│       └── ambush.json
│
├── ui/                           # User Interface
│   ├── streamlit_app.py         # Haupt-UI (Streamlit)
│   ├── components/
│   │   ├── map_view.py          # Kartenansicht
│   │   ├── unit_panel.py        # Einheitenübersicht
│   │   ├── order_interface.py   # Befehlseingabe
│   │   └── battle_log.py        # Gefechtsprotokoll
│   │
│   └── static/
│       ├── css/
│       └── js/
│
├── tests/                        # Tests
│   ├── unit/
│   ├── integration/
│   └── performance/
│
└── notebooks/                    # Jupyter Notebooks
    ├── doctrine_development.ipynb
    ├── combat_analysis.ipynb
    └── agent_training.ipynb
