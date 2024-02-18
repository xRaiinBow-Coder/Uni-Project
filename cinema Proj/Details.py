import os
import datetime
import time

def BookingTimes():
    time.sleep(0.5)
    os.system("cls")
    print("Bookings are between 01/01/2024 and 01/03/2024")
    when = input("What dates would you like to book? (DD/MM/YYYY): ")

    #selects dates which are hard coded because i want the user to input between jan and march
    # Also, this saves the input from (YourDate) and adds it to the receipt.
    #if invalid dates or format are entered, the program will restart untill the user inputs the correct times.
    startDate = datetime.datetime(2024, 1, 1)
    endDate = datetime.datetime(2024, 3, 1)
    while True:
        try:
            YourDate = datetime.datetime.strptime(when, "%d/%m/%Y").date()

            Today = datetime.date.today()

            if Today < startDate.date():
                print("Not Avliable")
            elif Today > endDate.date():
                print("Not avaliable")
            elif startDate.date() <= YourDate <= endDate.date():
                print("Congratualions, booking went through for you", YourDate.strftime("%d,%m, %Y"))
                with open("reciept.txt", "a") as file:
                    file.write(f"Booking Date: {YourDate.strftime('%d/%m/%Y')}\n")
                    file.close()
                    break
            else:
                print("invalid dates.")
                BookingTimes()
                break
        except ValueError:
            print("Error, wrong format")
            BookingTimes()
            break

    
    

