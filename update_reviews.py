from db import get_connection

def update_review(review_id, new_text):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE reviews SET review_text = %s WHERE id = %s"
    cursor.execute(query, (new_text, review_id))

    conn.commit()
    cursor.close()
    conn.close()
