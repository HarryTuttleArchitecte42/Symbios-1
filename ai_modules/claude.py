import os
from anthropic import AsyncAnthropic # Version Asynchrone obligatoire

async def query_claude(prompt, system_instruction="Tu es l'arbitre suprême de SynergyAI."):
    try:
        # On récupère la clé proprement depuis l'environnement
        client = AsyncAnthropic(api_key=os.getenv("CLAUDE_API_KEY"))
        
        message = await client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=2000,
            system=system_instruction,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except Exception as e:
        return f"ÉCHEC CLAUDE: {str(e)}"