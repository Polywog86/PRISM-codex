import sqlite3
import os

DB_FILE = "hive_notes.db"

def create_tables():
    #Create the necessary database tables if they do not exist.
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE NOT NULL,
        content TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        note_id INTEGER NOT NULL,
        tag TEXT NOT NULL,
        FOREIGN KEY (note_id) REFERENCES notes(id)
    )
    """)

    conn.commit()
    conn.close()
    
def add_tag(note_title, tag_id):
    #Adds a tag to a note.
    conn = sqlite3.connect("DB_FILE")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO tags (tag_id) VALUES (?)", (tag_id,))
    cursor.execute("SELECT id FROM tags WHERE note_title=?", (note_title,))
    tag_id = cursor.fetchone()[0]

    if note:  
        note_title: note[0] 
        cursor.execute("INSERT OR IGNORE INTO note_tag (note_id, tag_id) VALUES (?, ?)", (note_title, tag_id))
    
    
    conn.commit()
    conn.close()
    
def search_notes_by_tag(tag_id):
    #Search notes associated with a specific tag.
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT notes.title FROM notes
    JOIN note_tag ON notes.id = note-tag.note_id
    JOIN tags ON tags.id = note_tag.tag_id
    WHERE tags.tag_name = ?
    """, (tag_id,))

    results = cursor.fetchall()
    conn.close()
    return [row[0] for row in results]
    

db_folder = "database"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)


db_path = os.path.join(db_folder, "hive_note.db")

def search_notes_by_keyword(keyword):
    #Search notes containing a keyword in title or content.
    conn = sqlite3.connect("database/hive_note.db")
    cursor = conn.cursor()

    cursor.execute("SELECT title FROM notes WHERE title LIKE ? OR content LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()
    conn.close()
    return [row[0] for row in results]

try:
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tag_name TEXT NOT NULL UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS note_tag (
        note_id INTEGER,
        tag_id INTEGER,
        FOREIGN KEY (note_id) REFERENCES notes (id),
        FOREIGN KEY (tag_id) REFERENCES tags (id),
        PRIMARY KEY (note_id, tag_id)
    )
    ''')

    
    conn.commit()
    print("Database setup complete.")
    
except sqlite3.Error as e:
    print(f"Error: {e}")
    
finally:
    conn.close()

    conn = sqlite3.connect("database/hive_note.db")
    cursor = conn.cursor()




    


    
   




