import sqlite3
from sys import platform


def write_input_file():
    categories = get_categories()
    for category in categories:
        file_name = category[0] + ".txt"
        with open(file=f"{file_name}", mode="w", encoding="utf-8") as file:
            text = """ffconcat version 1.0"""
            videos = get_video_path(category[0])
            for e in videos:
                text += f"\nfile '{e[0]}'"
            text += f"\nfile {file_name}"
            print(text)
            file.write(text)


def connect_db():
    print(platform)
    if platform == "linux" or platform == "linux2":
        conn = sqlite3.connect("/usr/local/bin/botwithclips/utils/db_api/user.db")
    elif platform == "win32":
        conn = sqlite3.connect("C:\\Users\\KENT SZ\\PycharmProjects\\botwithclips\\utils\\db_api\\user.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    db = connect_db()
    db.cursor().execute("""CREATE TABLE IF NOT EXISTS videos(
    category TEXT,
    link TEXT NOT NULL UNIQUE,
    upload_date TEXT,
    path TEXT
    )""")
    db.commit()
    db.close()


def add_video(category, link, upload_date, path=None):
    sql = """INSERT INTO videos (category, link, upload_date, path) VALUES (?, ?, ?, ?)"""
    try:
        db = connect_db()
        db.cursor().execute(sql, (category, link, upload_date, path))
        db.commit()
        db.close()
        write_input_file()
    except sqlite3.IntegrityError:
        db.close()
        raise sqlite3.IntegrityError


def get_video_path(category):
    sql = """SELECT path FROM videos WHERE category==?"""
    db = connect_db()
    cur = db.cursor()
    cur.execute(sql, (category, ))
    res = cur.fetchall()
    return res


def get_categories():
    sql = """SELECT DISTINCT category FROM videos"""
    db = connect_db()
    cur = db.cursor()
    cur.execute(sql, )
    row = cur.fetchall()
    res = []
    for e in row:
        res.append(e)
    return res


if __name__ == "__main__":
    create_table()