import uvicorn
import os
import sys

# On s'assure que Python voit les dossiers 'logic' et 'ai_modules'
sys.path.append(os.getcwd())

if __name__ == "__main__":
    print("🚀 Démarrage de SynergyAI sur le port 8080...")
    # On pointe vers le module 'main' qui est dans le dossier 'synergyai-core'
    # On force le dossier de travail pour les templates
    uvicorn.run("synergyai-core.main:app", host="0.0.0.0", port=8080, reload=True)
