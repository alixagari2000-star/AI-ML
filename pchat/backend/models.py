from db import get_connection

def save_message(user_id: int, message: str):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO messages (user_id, message) VALUES (%s, %s)"
    cursor.execute(query, (user_id, message))
    conn.commit()
    cursor.close()
    conn.close()

def get_chat_history(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT message FROM messages WHERE user_id = %s ORDER BY created_at"
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [row[0] for row in rows]
