import asyncio
from ai_modules.claude import query_claude
from ai_modules.gemini import query_gemini
from ai_modules.mistral import query_mistral
from logic.gatekeeper import classify_intent
from logic.memory import store_interaction, get_recent_context

async def symbios_orchestrate(user_query):
    # 1. Analyse d'intention
    category = await classify_intent(user_query)
    print(f"DEBUG [Symbios-1] : Catégorie -> {category}")

    if category == "BASIQUE":
        return await query_gemini(user_query, "Réponds de manière concise et amicale.")

    # 2. Tier de Synergie (Gemini + Mistral)
    print("🧠 [Symbios-1] : Activation du mode Synergie...")
    
    # On exécute les deux en parallèle
    gemini_res, mistral_res = await asyncio.gather(
        query_gemini(user_query, "Fournis une analyse technique détaillée."),
        query_mistral(user_query, "Fournis une analyse critique et identifie les risques.")
    )

    # 3. Synthèse par le "Juge" (Claude)
    print("⚖️ [Symbios-1] : Claude synthétise la réponse finale...")
    
    context_for_judge = f"""
ANALYSE MODULE 1 (GEMINI):
{gemini_res}

ANALYSE MODULE 2 (MISTRAL):
{mistral_res}
"""

    system_prompt = """
Tu es le Juge Suprême de l'écosystème SynergyAI (Protocole Symbios-1). 
Ton rôle est de confronter et de synthétiser les analyses de deux modules experts : GEMINI et MISTRAL.

DIRECTIVES DE RÉDACTION :
1. CITATION EXPLICITE : Tu DOIS nommer tes sources. Utilise des marqueurs comme "[Selon Gemini...]", "[L'analyse de Mistral souligne...]", "[En croisant les deux...]".
2. ARBITRAGE : Si les deux experts divergent, ne lisse pas la réponse. Explique POURQUOI ils ne sont pas d'accord (ex: approche technique vs approche éthique).
3. STRUCTURE : 
   - Introduction (Synthèse flash de la situation)
   - Analyse Croisée (Le cœur du débat entre Gemini et Mistral)
   - Verdict Actionnable (Ta conclusion finale tranchée)
4. STYLE : Direct, froid, analytique. Pas de politesses inutiles.

CONTEXTE DES EXPERTS :
{expert_responses}
"""
    
    # --- NOUVELLE LOGIQUE DE MÉMOIRE ---
    # On récupère les 3 derniers échanges pour donner du contexte à Claude
    past_memory = get_recent_context(limit=3)

    # On enrichit le contexte de jugement avec l'historique
    enriched_context = f"""
HISTORIQUE DES ÉCHANGES PRÉCÉDENTS :
{past_memory if past_memory else "Aucun historique disponible."}

NOUVELLES ANALYSES DES EXPERTS :
{context_for_judge}
"""

    # 1. On prépare le prompt système final en injectant l'historique et les analyses
    full_system_instruction = system_prompt.replace("{expert_responses}", enriched_context)
    
    # 2. On appelle Claude (Le Juge)
    final_output = await query_claude(
        user_query, 
        full_system_instruction
    )
    
    # --- SAUVEGARDE EN MÉMOIRE ---
    # On enregistre cette interaction pour la prochaine fois
    store_interaction(user_query, final_output)
    
    # 3. On renvoie enfin le résultat à l'interface
    return final_output