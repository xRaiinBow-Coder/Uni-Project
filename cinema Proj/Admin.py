import sqlite3
import hashlib
import os

###Log in is case sensitive
###Log into the account - Username = admin
###Log into the account - Password = password


conn = sqlite3.connect("Admin.db")

conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
def CreateAdminAccount(conn, username, password):
    cursor = conn.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if len(username) == 0 or len(password) ==0:
        print("Invalid")
        return

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("Admin account created")

def AttemptedAdminLogin(conn):
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
        AttemptedAdminLogin(conn)

#log into an already made admin account to view prior bookings made by the customers.
def Admin():
    print("Admin log in...\n")
    AttemptedAdminLogin(conn)
    PriorBookings = input("Would you like to view user bookings? (Yes or No):").lower()
    if PriorBookings == "yes":
        with open("reciept.txt", "r") as file:
            booking = file.read()
            print(booking)
        
        carryon = input("would you like to 1) quit or 2) continue into the program? (1,2): ")
        if carryon == 1:
            print("Bye")
            quit()
        elif carryon == 2:
            os.system("cls")
            pass
    
    elif PriorBookings == "no":
        print("This program will exit, Thank you.")
        quit()

