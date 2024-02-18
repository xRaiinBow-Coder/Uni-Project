import sqlite3
import hashlib

conn = sqlite3.connect("account.db")

#this code creates the table in the database if it doesnt already exist
conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

#creating the user account
def CreateUserAccount(conn, username, password):
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("user account created")

#login to the account you have just created with a fale safe to make sure the user inputs the correct details
def AttemptedLogin(conn):
    username = input("Username: ")
    password = input("Password: ")
    cursor = conn.cursor()
    hashed_password = password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("SELECT * FROM users WHERE username =? AND password=?", (username, hashed_password))
    user = cursor.fetchone()
    if user:
        print("Success")
    else:
        print("Invalid")
        AttemptedLogin(conn)




    
    
    

