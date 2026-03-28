import uvicorn
import os
import sys

# On s'assure que Python regarde dans le dossier courant pour trouver 'logic'
sys.path.append(os.getcwd())

if __name__ == "__main__":
    print("🚀 DÉMARRAGE DE SYNERGY-AI (SYMBIOS-1)...")
    try:
        uvicorn.run("synergyai-core.main:app", host="0.0.0.0", port=8080, reload=True)
    except Exception as e:
        print(f"❌ ERREUR DE DÉMARRAGE : {e}")
