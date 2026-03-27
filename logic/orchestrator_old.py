import asyncio
from ai_modules.claude import query_claude
from ai_modules.gemini import query_gemini
from logic.gatekeeper import classify_intent

async def symbios_orchestrate(user_query):
    """
    Cerveau de SynergyAI : Gère le flux intelligent entre les IA.
    """
    # 1. Le Gatekeeper décide du niveau d'effort
    category = await classify_intent(user_query)
    print(f"DEBUG [Symbios-1] : Catégorie détectée -> {category}")

    if category == "BASIQUE":
        # On ne sort pas l'artillerie lourde pour un "Bonjour"
        # On utilise Gemini ou Mistral directement (plus rapide/moins cher)
        return await query_gemini(user_query, "Réponds de manière concise et amicale.")

    # 2. TIER COMPLEXE : Activation de la Synergie
    print("🧠 [Symbios-1] : Activation du mode Synergie (Multi-IA)...")
    
    # On lance Gemini et une autre IA (ou Mistral si tu l'as configuré) en parallèle
    # return_exceptions=True évite que tout crash si une API tombe
    responses = await asyncio.gather(
        query_gemini(user_query, "Analyse technique et contextuelle."),
        # Ici on pourrait ajouter query_mistral(user_query)
        return_exceptions=True
    )

    # 3. Claude intervient en tant que Juge et Synthétiseur
    context_for_judge = f"Voici les analyses brutes de mes modules :\n{responses}"
    
    system_prompt = """
    Tu es le Cerveau Final de SynergyAI. 
    Ta mission : Synthétiser les analyses de Gemini et Mistral pour donner LA réponse parfaite.
    Élimine les répétitions, corrige les erreurs et sois direct.
    """
    
    final_synthesis = await query_claude(user_query + "\n\n" + context_for_judge, system_prompt)
    
    return final_synthesis