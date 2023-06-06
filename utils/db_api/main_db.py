import sqlite3

def connect_db():
    conn = sqlite3.connect("C:\\Users\\KENT SZ\\PycharmProjects\\botwithclips\\utils\\db_api\\user.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    db.cursor().execute("""CREATE TABLE IF NOT EXISTS user(
    id TEXT NOT NULL UNIQUE,
    permission INTEGER DEFAULT 0)""")
    db.commit()
    db.close()


def access_verification(user_id: int):
    sql = "SELECT id, permission FROM user WHERE id == ?"
    db = connect_db()
    cur = db.cursor()
    cur.execute(sql, (user_id,))
    res = cur.fetchone()
    if res:
        return res


def add_user(user_id, permission):
    sql = "INSERT INTO user (id, permission) VALUES (?, ?)"
    db = connect_db()
    cur = db.cursor()
    cur.execute(sql, (user_id, permission))
    db.commit()
    db.close()


if __name__ == "__main__":
    create_db()