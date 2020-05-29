import sqlite3 as sql
from os import path

# root name, direct name, relative path name
ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    # create connection to db
    conn = sql.connect(path.join(ROOT, 'database.db'))

    # cursor - goes to what we need instead of grabbing whole db
    cur = con.cursor()
    # execute raw sql syntax to insert post to db 
    cur.execute('insert into posts (name, content) values(?, ?)', (name, content)) 
    
    conn.commit()
    conn.close()

def get_posts():
    conn = sql.connect(path.join(ROOT, 'database.db'))
    cur = conn.cursor()

    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts