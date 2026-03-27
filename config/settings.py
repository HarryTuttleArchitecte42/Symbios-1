import os

# Récupération des clés API depuis les variables d'environnement du système
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Configuration des modèles par défaut
DEFAULT_CLAUDE_MODEL = "claude-3-haiku-20240307"

# Sécurité : Vérification de la présence de la clé principale
if not CLAUDE_API_KEY:
    print("⚠️ Attention : CLAUDE_API_KEY n'est pas configurée dans le terminal.")