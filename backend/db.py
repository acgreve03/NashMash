# This file manages the database connection and all song queries 
import sqlite3

#establishes connection to db
def connect_db():
    sqlite3.connect("songs.db")


#create table
def create_table():

    con = connect_db()

    #object that executes SQL statements and fetches results from SQL queries 
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                TITLE TEXT  NOT NULL,
                ARTIST TEXT NOT NULL,
                BPM_LOW REAL,
                BPM_HIGH REAL
                KEY TEXT
                MODE TEXT)''')
    
    con.commit()
    con.close()


#function to insert song
def insert_song(title, artist, bpm, key, mode):
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO songs (title, artist, bpm, key, mode) VALUES (?, ?, ?, ?, ?)",
                (title, artist, bpm, key, mode))
    con.commit()
    con.close()


#function to retrieve a song
def get_song(title):
    con = connect_db()
    cur = con.cursor()

    cur.execute("SELECT * FROM songs WHERE title LIKE ?", ('%' + title + '%',))
    song = cur.fetchone()
    con.close()

    return song









