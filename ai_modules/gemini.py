import os
import vertexai
from vertexai.generative_models import GenerativeModel

# On initialise avec une sécurité si le projet n'est pas détecté
project_id = os.getenv("GOOGLE_CLOUD_PROJECT") or "ton-project-id-ici"
vertexai.init(project=project_id, location="europe-west9")

async def query_gemini(prompt, system_instruction=""):
    try:
        model = GenerativeModel("gemini-2.0-flash-001")
        # Appel ASYNC pour ne pas bloquer l'orchestrateur
        response = await model.generate_content_async(
            prompt,
            generation_config={"max_output_tokens": 2048}
        )
        return response.text
    except Exception as e:
        return f"Erreur Gemini : {str(e)}"