from db import get_connection

def fetch_old_reviews():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT id, review_text, review_date
        FROM reviews
        WHERE YEAR(review_date) < 2023
    """
    cursor.execute(query)
    reviews = cursor.fetchall()

    cursor.close()
    conn.close()
    return reviews

print(fetch_old_reviews())