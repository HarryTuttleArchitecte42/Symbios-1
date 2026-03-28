import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse
# IMPORT DE TON MOTEUR RÉEL
from logic.orchestrator import symbios_orchestrate
from logic.database import init_db, get_all_specs 
from logic.memory import init_memory_db

app = FastAPI()
# Initialisation des moteurs de données
init_db()           # Ta base existante
init_memory_db()    # Ta nouvelle mémoire persistante

# Chemin absolu vers le dossier templates
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )
async def symbios_logic_augmented(query: str):
    yield {"data": "🌀 **[SYNERGY AI]** Initialisation du protocole Symbios-1...\n\n"}
    try:
        final_response = await symbios_orchestrate(query)
        yield {"data": f"✅ **[RÉSULTAT FINAL]**\n\n{final_response}"}
    except Exception as e:
        yield {"data": f"❌ **[ERREUR SYSTÈME]** : {str(e)}"}

@app.get("/ask")
async def ask(request: Request, prompt: str):
    return EventSourceResponse(symbios_logic_augmented(prompt))
