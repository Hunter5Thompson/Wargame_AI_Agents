# Wargame AI Agents 🎯

*Ein moderner Ansatz auf das alte preußische Kriegsspiel - mit Small Language Models, LangGraph und MCP Servern*

## 🎖️ Das Preußische Erbe

Das preußische Kriegsspiel (*Kriegsspiel*), entwickelt 1824 von Georg Leopold von Reiswitz, revolutionierte die militärische Ausbildung durch strukturierte Simulation. Diese Tradition führen wir fort - mit KI-Agenten als Kommandeure, die verschiedene Militärdoktrinen verkörpern und realistische taktische Entscheidungen treffen.

> *"Der Krieg ist das Gebiet der Ungewißheit; drei Viertel derjenigen Faktoren, auf welche das Handeln im Kriege gebaut wird, liegen mehr oder weniger im Nebel einer größeren oder geringeren Ungewißheit."* - Carl von Clausewitz

## 🚀 Vision

Dieses Projekt implementiert ein **Proof of Concept** für KI-gesteuerte Kriegssimulation, wobei:
- **Small Language Models** als taktische Kommandeure agieren
- **LangGraph** komplexe Entscheidungsketten orchestriert  
- **MCP Server** historische Daten und Doktrinen bereitstellen
- **Realistische Militärdoktrinen** (Vietnam-Ära) das Verhalten prägen

## 🏗️ Architektur

```
📁 prussian-wargame/
├── 🎯 core/                    # Simulationskern
│   ├── domain/                 # Militärische Entitäten
│   ├── simulation/             # Physics Engine
│   └── analytics/              # Kampfmodelle (Lanchester etc.)
├── 🤖 agents/                  # KI-Kommandeure
│   ├── doctrines/             # US/NVA/ARVN/VC Doktrinen  
│   ├── commanders/            # Kommandoebenen
│   └── graphs/                # LangGraph Entscheidungsbäume
├── 🌐 mcp_servers/            # Datenserver
│   ├── historical_data/       # Schlacht-Datenbank
│   ├── doctrine_server/       # Taktik-Wissensbasis
│   └── realtime_server/       # Live-Updates
├── 🧠 models/                 # LLM Konfiguration
├── 🎮 scenarios/              # Historische Szenarien
└── 📊 ui/                     # Streamlit Interface
```

## 🎭 KI-Agenten Portfolio

### 🇺🇸 **US Forces**
- **Air Mobile Doctrine**: Hubschrauber-gestützte Manöver
- **Fire Support Coordination**: Präzise Artillerie-/Luftunterstützung
- **Advanced Logistics**: Überlegene Versorgungsketten

### 🇻🇳 **NVA (North Vietnamese Army)**
- **People's War Strategy**: Langzeit-Zermürbungstaktik
- **Tunnel Systems**: Unterirdische Operationsbasen
- **Mass Infantry Assaults**: Koordinierte Großangriffe

### 🇻🇳 **ARVN (Army of Vietnam)**
- **Defensive Operations**: Befestigte Stellungen halten
- **Local Knowledge**: Terrain-/Bevölkerungsverständnis
- **US Equipment Integration**: Amerikanische Waffentechnik

### 🌿 **Viet Cong**
- **Guerrilla Warfare**: Hinterhalt und Sabotage
- **Civilian Blend**: Tarnung in der Zivilbevölkerung
- **Booby Traps**: Improvisierte Sprengfallen

## 🧮 Simulationsmodelle

### **Lanchester'sche Gesetze**
Mathematische Modellierung von Kampfkraft und Verlustprognosen

### **OODA-Loop Integration**
- **Observe**: Aufklärungs- und Sensordaten
- **Orient**: Situationsbewertung mit historischem Kontext
- **Decide**: Doktrin-basierte Entscheidungsfindung  
- **Act**: Befehlsausführung und Feedback-Loop

### **Clausewitz'sche Prinzipien**
- **Nebel des Krieges**: Unvollständige Information
- **Friktion**: Unvorhersehbare Störfaktoren
- **Schwerpunkt**: Konzentration der Kräfte

## 🎯 Kernfeatures

### **Realistische Kommandostrukturen**
```python
# Hierarchische Befehlskette
Strategic Command (Division/Corps)
    ↓
Operational Command (Brigade/Regiment)  
    ↓
Tactical Command (Battalion/Company)
    ↓
Squad Leaders (Platoon/Squad)
```

### **Dynamische Gefechtssimulation**
- **Ballistik & Physik**: Realistische Projektilbahnen
- **Line-of-Sight**: Geländebasierte Sichtlinien
- **Wettereffekte**: Einfluss auf Sicht und Bewegung
- **Moral & Müdigkeit**: Psychologische Faktoren

### **Spezialisierte KI-Rollen**
- **🎖️ Platoon Leader**: Schnelle taktische Entscheidungen
- **💥 Fire Support Officer**: Artillerie-Koordination
- **🔍 Intel Analyst**: Feindlagebeurteilung
- **📦 Logistics Officer**: Versorgungsplanung

## 🎮 Vietnam-Szenarien

### **Da Nang 1966**
- **US Marines** vs **NVA/VC** um strategischen Flughafen
- Dschungelkampf mit Helikopter-Unterstützung
- Komplexe Zivilisten-/Kombattanten-Unterscheidung

### **Weitere Szenarien**
- **Meeting Engagement**: Zufällige Feindberührung
- **Defensive Operations**: Stützpunkt-Verteidigung  
- **Ambush Scenarios**: Hinterhalt-Situationen

## 🛠️ Technologie-Stack

```yaml
Core Engine:
  - Python 3.11+
  - LangGraph (Agentenorchestierung)
  - MCP Protocol (Datenserver)
  
AI Models:
  - Ollama (Lokale LLM Hosting)
  - Quantisierte Modelle (Effizienz)
  - Custom Military Prompts

Simulation:
  - NumPy (Numerische Berechnungen)
  - GeoPandas (Geländeanalyse)
  - NetworkX (Kommunikationslinien)

Interface:
  - Streamlit (Web UI)
  - Plotly (Interaktive Karten)
  - WebGL (3D Visualisierung)

Infrastructure:
  - Docker Compose
  - Redis (Caching)
  - SQLite (Historische Daten)
```

## 🚀 Quick Start

```bash
# Repository klonen
git clone https://github.com/your-org/wargame-ai-agents.git
cd wargame-ai-agents

# Environment Setup
cp .env.template .env
pip install -r requirements.txt

# Ollama Models herunterladen
ollama pull llama3.2:3b
ollama pull mistral:7b

# Services starten
docker-compose up -d

# Simulation starten
streamlit run ui/streamlit_app.py
```

## 📊 Metriken & Analytics

### **Gefechtsanalyse**
- **Casualty Ratios**: Verlustvergleiche
- **Terrain Control**: Geländebeherrschung über Zeit
- **Supply Efficiency**: Logistik-Performance
- **Command Latency**: Entscheidungsgeschwindigkeit

### **KI-Agent Performance**
- **Decision Quality**: Taktische Angemessenheit
- **Doctrine Adherence**: Treue zur Militärdoktrin  
- **Adaptability**: Reaktion auf unerwartete Situationen
- **Resource Utilization**: Effizienter Ressourceneinsatz

## 🎯 Roadmap

### **Phase 1: Foundation** ✅
- [x] Basis-Simulationsengine
- [x] Einfache KI-Agenten
- [x] Streamlit Prototyp

### **Phase 2: Intelligence** 🔄
- [ ] LangGraph Integration
- [ ] MCP Server Implementation
- [ ] Doktrin-spezifische Agenten
- [ ] Vietnam Szenario

### **Phase 3: Sophistication** 📋
- [ ] Multi-Agent Negotiation
- [ ] Real-time Weather/Intel Feeds
- [ ] Advanced Physics (Ballistics)
- [ ] Machine Learning Integration

### **Phase 4: Scale** 🚀
- [ ] Multi-Theater Operations
- [ ] Historical Battle Recreation
- [ ] Educational Interface
- [ ] Competition Mode

## 🤝 Contribution

Wir suchen Verstärkung in:
- **🎖️ Militärhistorikern**: Doktrin-Authentizität
- **🤖 AI Engineers**: LLM Optimierung  
- **⚙️ Simulation Devs**: Physics/Mathematics
- **🎮 Game Designers**: User Experience

## 📚 Literatur & Inspiration

- **"Vom Kriege"** - Carl von Clausewitz
- **"The Art of War"** - Sun Tzu  
- **"On War"** - B.H. Liddell Hart
- **"We Were Soldiers Once... and Young"** - Harold G. Moore
- **"The Face of Battle"** - John Keegan

## 📄 Lizenz

MIT License - Siehe [LICENSE](LICENSE) für Details.

---

*"In der Beschränkung zeigt sich erst der Meister, und das Gesetz nur kann uns Freiheit geben."*  
**- Goethe** (über die Kunst der Simulation)

🎯 **[Live Demo]** | 📖 **[Dokumentation]** | 💬 **[Discord Community]** | 🐛 **[Issues]**
