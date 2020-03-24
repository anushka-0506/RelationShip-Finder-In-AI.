import sqlite3

def connect():
    conn =sqlite3.connect("Relations.db")
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Relation (id INTEGER PRIMARY KEY,  Name1 text, Name2 text, Relationship text) ")
    conn.commit()
    conn.close()


def insert( Name1, Name2, Relationship):
    conn =sqlite3.connect("Relations.db")
    cur= conn.cursor()
    cur.execute("INSERT INTO Relation VALUES(NULL, ?,?,?)", (Name1, Name2, Relationship))
    conn.commit()
    conn.close()


def view():
    conn =sqlite3.connect("Relations.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM Relation")
    rows =cur.fetchall()
    conn.close()
    return rows

def search( Name1="", Name2="", Relationship=""):
    conn =sqlite3.connect("Relations.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM Relation WHERE  Name1=? AND Name2=? OR Relationship=?",( Name1, Name2, Relationship))
    rows =cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn =sqlite3.connect("Relations.db")
    cur= conn.cursor()
    cur.execute("DELETE FROM Relation WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,  Name1, Name2, Relationship ):
    conn =sqlite3.connect("Relations.db")
    cur= conn.cursor()
    cur.execute("UPDATE Relation SET  Name1=?, Name2=?, Relationship=? WHERE id=?",( Name1, Name2, Relationship))
    conn.commit()
    conn.close()

connect()

