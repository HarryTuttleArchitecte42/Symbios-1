import sqlite3
import os

DB_PATH = "synergy_memory.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Table pour les connaissances persistantes (préférences, règles système)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_knowledge (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    # Table pour l'historique des échanges (mémoire court/moyen terme)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# --- GESTION DES CONNAISSANCES FIXES ---

def save_spec(key, value):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO user_knowledge (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

def get_all_specs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT key, value FROM user_knowledge")
    specs = cursor.fetchall()
    conn.close()
    return "\n".join([f"- {s[0]}: {s[1]}" for s in specs])

# --- GESTION DE L'HISTORIQUE CONTEXTUEL ---

def add_chat_message(role, content):
    """Enregistre un message (user ou assistant) dans la base."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chat_history (role, content) VALUES (?, ?)", (role, content))
    conn.commit()
    conn.close()

def get_recent_history(limit=6):
    """Récupère les derniers échanges pour donner du contexte aux IA."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # On prend les X derniers messages
    cursor.execute("SELECT role, content FROM chat_history ORDER BY timestamp DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    # On sort de la fonction précédente ici

def get_relevant_context(user_query, threshold=0.2):
    """
    Analyse si les connaissances stockées sont pertinentes pour la question.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT key, value FROM user_knowledge")
    all_knowledge = cursor.fetchall()
    conn.close()

    relevant_bits = []
    # On transforme la question en un ensemble de mots-clés
    query_keywords = set(user_query.lower().split())

    for key, value in all_knowledge:
        # Score de pertinence simple basé sur l'intersection des mots
        content_words = set(f"{key} {value}".lower().split())
        intersection = query_keywords.intersection(content_words)
        
        # Si la pertinence est suffisante, on garde
        if len(query_keywords) > 0 and (len(intersection) / len(query_keywords)) >= threshold:
            relevant_bits.append(f"[{key}]: {value}")

    return "\n".join(relevant_bits) if relevant_bits else "Aucun contexte spécifique pertinent."

def get_recent_history(limit=6):
    """Récupère les derniers échanges pour donner du contexte aux IA."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT role, content FROM chat_history ORDER BY timestamp DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()

    # On remet dans l'ordre chronologique
    history = ""
    for role, content in reversed(rows):
        history += f"{role.upper()}: {content}\n"
    return history