import asyncio

async def classify_intent(user_query):
    """
    FORCE le mode COMPLEXE pour contourner les erreurs d'authentification Google.
    """
    print("DEBUG [Gatekeeper] : Bypass activé -> Direction CLAUDE")
    return "COMPLEXE"