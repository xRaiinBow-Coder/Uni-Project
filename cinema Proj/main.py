#importing from other functions and modules
from movies import ShowMovies 
from log import CreateUserAccount, AttemptedLogin
from prices import Tickets
from Details import BookingTimes
from Admin import Admin
import os
import sqlite3
import time




conn = sqlite3.connect("account.db")
MovieSelection = ShowMovies

#Admin log in to view the prior bookings
AdminAccount = input("Do you want to log into the Admin account? (Yes or No): ").lower()
if AdminAccount == "yes":
    Admin()
elif AdminAccount == "no":
    pass
else:
    quit()

#User account log in or making an account to book a movie at the cinema
os.system("cls")
account = input("welcome to the cinema, Do you have an account with us?\n1) Log in\n2) No\nEnter (1,2): ")
if account == "1":   
    AttemptedLogin(conn)
    
elif account == "2":
    accounts = input("would you like to creat an account? or exit?: (1, 2): ")
    if accounts == "1":
        new_username = input("please input a username: ")
        new_password = input("please input a password: ")
        CreateUserAccount(conn, new_username, new_password)
        
        time.sleep(0.5)
        carryOn = input("Thank you for creating an account with us, would you like to log in: (yes or no) ").lower()
        if carryOn == "yes":
            AttemptedLogin(conn)
        else:
            quit()
    elif accounts == "2":
        conn.close()
        quit()
else:
    quit()


os.system("cls")

print("Thank you for logging in, before i can book you a movie, i will need your user information.")
#input personal details for the reciept which will get shown to the admin.
#if you the user puts no information in, the code will reset untill they enter the information required.
def personalDetails():

    fname = input("please enter your first name: ")
    Sname = input("Please enter your surname: ")
    Email = input("please enter your email: ")
    phone = input("please enter your phone number: ")

    if len(fname) == 0 or len(Sname) == 0  or len(Email) == 0 or len(phone) == 0:
        print("\nInput was empty try again\n")
        personalDetails()
    else:
        with open("reciept.txt", "a") as file:
            file.write(f"\nBooking - \nFirst Name: {fname}\nSurName: {Sname}\nEmail: {Email}\nPhone: {phone}")

personalDetails()


os.system("cls")

#This is where the cinema starts running
cinema = input("Would you like to book a movie? (Yes or No): ").lower()
if cinema == "yes":
    print("Great, here you go...")
    ShowMovies()
    time.sleep(1)
    BookingTimes()
    time.sleep(1)
    Tickets()
else:
    pass

print("Thank you for using our cinema, we hope you have a great stay.")
os.system("cls")



