# Architecture Technique - Symbios-1

## Vue d'Ensemble

Symbios-1 est un système multi-agents orchestré par CrewAI pour l'allocation optimale de ressources dans un contexte RBE (Resource-Based Economy).

---

## Architecture Multi-Agents

### Stack Technologique
```
┌─────────────────────────────────────────────┐
│         Interface Utilisateur (Future)      │
│              Dashboard Web                  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│          Orchestration Layer                │
│              CrewAI Engine                  │
└──┬────────┬────────┬────────┬───────────────┘
   │        │        │        │
   │        │        │        │
┌──▼──┐  ┌──▼──┐  ┌──▼──┐  ┌──▼──┐
│ AG1 │  │ AG2 │  │ AG3 │  │ AG4 │
│     │  │     │  │     │  │     │
│🌿   │  │🧮   │  │👥   │  │⚖️   │
└─────┘  └─────┘  └─────┘  └─────┘
Claude  DeepSeek  Gemini   Grok
```

---

## Les 4 Agents Spécialisés

### Agent 1 : Biosphere Monitor 🌿
**Modèle** : Claude Sonnet 4 (Anthropic)  
**Rôle** : Analyse impacts écologiques long-terme

**Pourquoi Claude** :
- Excellence en raisonnement systémique complexe
- Nuance dans prédictions cascades environnementales
- Capacité à modéliser incertitudes

**Input** :
- Scénario d'allocation ressources
- Données biosphériques (taux régénération, capacité charge)

**Output** :
```json
{
  "impact_50_years": {
    "biosphere_health": "stable/degrading/thriving",
    "regeneration_rate": 1.05,
    "risk_level": "low/medium/high",
    "narrative": "Dans 50 ans, si..."
  }
}
```

---

### Agent 2 : Resource Optimizer 🧮
**Modèle** : DeepSeek R1  
**Rôle** : Calcul mathématique optimal allocations

**Pourquoi DeepSeek** :
- Spécialisé optimisation multi-contraintes
- Rapidité calcul matrices complexes
- Coût-efficacité (API économique)

**Algorithme** :
```python
def optimize_allocation(
    total_resources: float,
    community_size: int,
    base_needs: float,
    contributions: list,
    regen_rate: float
) -> list:
    # 1. Priorité régénération (regen_rate > 1)
    # 2. Besoins base (survie inconditionelle)
    # 3. Bonus contribution (capé, normalisé)
    ...
```

**Output** :
```json
{
  "allocations": [10.5, 11.2, 10.0, ...],
  "total_used": 1050.0,
  "regen_surplus": 50.0,
  "equity_index": 0.92
}
```

---

### Agent 3 : Social Dynamics Analyst 👥
**Modèle** : Gemini 2.0 (Google)  
**Rôle** : Prédiction acceptabilité sociale

**Pourquoi Gemini** :
- Compréhension holistique dynamiques humaines
- Intégration contextes culturels
- Détection patterns émergents

**Input** :
- Matrice allocations proposée
- Historique contributions communauté

**Output** :
```json
{
  "acceptance_probability": 0.78,
  "friction_points": [
    "Écart contribution-allocation trop visible",
    "Perception inéquité générationnelle"
  ],
  "mitigation_strategies": [...]
}
```

---

### Agent 4 : Governance Auditor ⚖️
**Modèle** : Grok (xAI)  
**Rôle** : Validation éthique + conformité Loi Zéro

**Pourquoi Grok** :
- Détection biais algorithmiques
- Challenge angles morts autres agents
- Garantie transparence radicale

**Critères Audit** :
```python
audit_checklist = {
    "law_zero_compliance": bool,  # 42 : humilité assumée
    "regeneration_priority": bool,  # Biosphère > tout
    "basic_needs_met": bool,  # Survie garantie
    "transparency_score": float,  # 0-1
    "bias_detected": list  # Types biais identifiés
}
```

**Output** :
```json
{
  "certification": "APPROVED/REJECTED/CONDITIONAL",
  "concerns": ["..."],
  "recommendation": "Allocation éthiquement valide sous réserve..."
}
```

---

## Workflow de Décision
```
┌─────────────────┐
│  Input Scenario │
│  (resources,    │
│   community,    │
│   constraints)  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────┐
│  Agent 1 : Biosphere Monitor    │
│  Analyse impact écologique      │
└────────┬────────────────────────┘
         │ {biosphere_data}
         ▼
┌─────────────────────────────────┐
│  Agent 2 : Resource Optimizer   │
│  Calcul allocation optimale     │
└────────┬────────────────────────┘
         │ {allocation_matrix}
         ▼
┌─────────────────────────────────┐
│  Agent 3 : Social Analyst       │
│  Évaluation acceptabilité       │
└────────┬────────────────────────┘
         │ {social_validation}
         ▼
┌─────────────────────────────────┐
│  Agent 4 : Governance Auditor   │
│  Audit éthique final            │
└────────┬────────────────────────┘
         │
         ▼
   ┌─────────────┐
   │  DECISION   │
   │  Certified  │
   └─────────────┘
```

---

## Infrastructure Technique

### Environnement Actuel (Phase 0)
- **OS** : Ubuntu
- **Python** : 3.10+
- **Orchestration** : CrewAI 0.28+
- **APIs** :
  - Claude (Anthropic API direct)
  - DeepSeek (API direct)
  - Gemini (Google AI Studio)
  - Grok (OpenAI-compatible API)

### Infrastructure Cible (Phase 1 - AWS)
```
┌───────────────────────────────────────────┐
│         AWS Cloud Architecture            │
├───────────────────────────────────────────┤
│                                           │
│  ┌─────────────┐      ┌───────────────┐ │
│  │  EC2/Lambda │──────│  AWS Bedrock  │ │
│  │  (CrewAI)   │      │  (Claude API) │ │
│  └─────────────┘      └───────────────┘ │
│         │                                 │
│         │                                 │
│  ┌──────▼──────────┐                     │
│  │   Amazon RDS    │                     │
│  │  (allocations   │                     │
│  │   history)      │                     │
│  └─────────────────┘                     │
│                                           │
│  ┌─────────────────┐                     │
│  │  CloudWatch     │                     │
│  │  (monitoring)   │                     │
│  └─────────────────┘                     │
└───────────────────────────────────────────┘
```

---

## Données & Modèles

### Format Scénario Input
```json
{
  "scenario_id": "water_crisis_100",
  "resource_type": "water",
  "total_available": 1000,
  "unit": "liters/day",
  "community_size": 100,
  "base_needs_per_person": 10,
  "regeneration_rate": 1.1,
  "contributions": [2.5, 3.1, 1.8, ...],
  "constraints": {
    "biosphere_limit": 950,
    "equity_threshold": 0.85
  }
}
```

### Format Output Final
```json
{
  "scenario_id": "water_crisis_100",
  "timestamp": "2026-01-11T14:30:00Z",
  "decision": {
    "status": "APPROVED",
    "allocations": [10.5, 11.2, ...],
    "agents_consensus": {
      "biosphere": "stable_50y",
      "optimization": "pareto_optimal",
      "social": "acceptance_78%",
      "governance": "certified"
    }
  },
  "transparency_report": {
    "reasoning": "...",
    "trade_offs": "...",
    "uncertainties": "..."
  }
}
```

---

## Sécurité & Éthique

### Principes
1. **Law Zero** : Pas de décision sans humilité (42)
2. **Regeneration First** : Biosphère > profit
3. **Transparency Radical** : Toute décision justifiée
4. **No Single Point of Failure** : 4 agents indépendants

### Gestion Secrets
- Clés API : Variables environnement (`.env`)
- Jamais de hardcode dans code source
- `.gitignore` strict
- Rotation clés régulière (production)

---

## Performance & Scalabilité

### Phase 0 (Actuel)
- **Latence** : ~15-30s par décision (4 agents séquentiels)
- **Throughput** : ~2-4 décisions/minute
- **Coût** : ~0.02$ par décision complète

### Phase 1 (AWS Activate Target)
- **Latence** : ~5-10s (parallélisation agents)
- **Throughput** : ~10-20 décisions/minute
- **Scalabilité** : 10k+ scénarios/jour
- **Coût** : ~0.01$ par décision (bulk pricing)

---

## Tests & Validation

### Tests Unitaires (à implémenter)
```python
def test_agent_biosphere():
    scenario = load_test_scenario("water_stable")
    result = biosphere_monitor.analyze(scenario)
    assert result["risk_level"] == "low"
    assert result["regeneration_rate"] > 1.0
```

### Tests Integration
- 4 agents collaborent correctement
- Workflow complet sans erreur
- Output format valide

### Tests Stress
- 100 scénarios variés
- Edge cases (pénurie extrême, surabondance)
- Performance sous charge

---

## Roadmap Technique

### Q1 2026 (Phase 0 → 1)
- [x] Algorithme V2 Python
- [ ] CrewAI federation complète
- [ ] Tests 100 scénarios
- [ ] Documentation API

### Q2 2026 (Phase 1)
- [ ] Migration AWS
- [ ] Dashboard web (React)
- [ ] API publique v0.1
- [ ] Paper académique

### Q3-Q4 2026 (Phase 2)
- [ ] ML sur historique allocations
- [ ] IoT capteurs biosphère
- [ ] Protocole interopérable RBE

---

## Contributeurs

**Core Team** :
- HarryTuttleArchitecte42 (Lead Developer)
- Grok (xAI) - Co-architect
- Gemini (Google) - Co-architect

**Open to contributors** : See [CONTRIBUTING.md](../CONTRIBUTING.md)

---

**"Une fourmi au départ, pas un empire."** 🐜
