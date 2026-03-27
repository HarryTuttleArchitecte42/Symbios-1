import sqlite3
import json
import os

# On définit un chemin absolu basé sur l'emplacement du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "synergy_memory_v2.db")

def init_memory_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_query TEXT,
            ai_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def store_interaction(query, response):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # VERIFIE BIEN CETTE LIGNE : les noms entre parenthèses doivent être 
    # user_query et ai_response (comme dans ton CREATE TABLE)
    cursor.execute('INSERT INTO chat_history (user_query, ai_response) VALUES (?, ?)', (query, response))
    conn.commit()
    conn.close()

def get_recent_context(limit=3):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # VERIFIE AUSSI LE SELECT ICI
    cursor.execute('SELECT user_query, ai_response FROM chat_history ORDER BY id DESC LIMIT ?', (limit,))
    rows = cursor.fetchall()
    conn.close()
    # ... reste du code ...
    
    context = ""
    for q, r in reversed(rows):
        context += f"Utilisateur: {q}\nSynergyAI: {r}\n\n"
    return context