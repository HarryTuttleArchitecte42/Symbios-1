import asyncio
import os
import sys

# On force Python à regarder dans le dossier courant pour trouver 'logic', 'ai_modules', etc.
sys.path.append(os.getcwd())

from logic.orchestrator import symbios_orchestrate

async def test():
    print("\n" + "="*40)
    print("--- TEST DE L'INTELLIGENCE SYMBIOS-1 ---")
    print("="*40)
    
    # Vérification de la clé
    #key = os.getenv("CLAUDE_API_KEY")
    #if not key or key == "AA":
       # print("❌ ERREUR : La clé CLAUDE_API_KEY est absente ou invalide ('AA').")
       # print("Tape : export CLAUDE_API_KEY='ta_vraie_clé'")
       # return

    query = "Explique-moi l'intérêt de la synergie entre Claude et Gemini."
    print(f"\n[Harry] : {query}")
    print("\n⏳ Symbios-1 réfléchit (Appel Multi-IA)...")
    
    try:
        response = await symbios_orchestrate(query)
        print(f"\n[SynergyAI] : \n{response}")
    except Exception as e:
        print(f"\n❌ Erreur pendant le test : {e}")

if __name__ == "__main__":
    asyncio.run(test())
