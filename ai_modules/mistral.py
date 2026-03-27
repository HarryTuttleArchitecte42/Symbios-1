import os
import sys

# 1. On force l'accès au client profond du SDK v2.x
try:
    from mistralai.client import Mistral
except ImportError:
    try:
        # Fallback pour certaines variantes d'installations
        from mistralai import Mistral
    except ImportError:
        Mistral = None

async def query_mistral(prompt, system_instruction="Tu es un assistant technique expert."):
    api_key = os.getenv("MISTRAL_API_KEY")
    
    if Mistral is None:
        return "ERREUR CRITIQUE: Le SDK Mistral est mal installé (Namespace Error). Relancez 'pip install --upgrade mistralai'."
    
    if not api_key:
        return "ERREUR MISTRAL: MISTRAL_API_KEY non configurée dans l'environnement."

    try:
        # Initialisation du client
        client = Mistral(api_key=api_key)
        
        # Appel asynchrone spécifique à la v2
        response = await client.chat.complete_async(
            model="mistral-small-latest",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"ÉCHEC MISTRAL (v2): {str(e)}"