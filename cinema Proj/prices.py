import os
import time

#Pricings per age group depending on their screen choice
def Tickets():
    try:
        price = {
            "Student":{"2D": 8.00, "3D": 9.00, "IMAX": 13.00}, 
            "Teenager": {"2D": 6.00, "3D": 7.00, "IMAX": 12.00},
            "Child": {"2D": 4.00, "3D": 7.00, "IMAX": 10.00},
            "Adult": {"2D": 10.00, "3D": 11.00, "IMAX": 15.00}
        }

        time.sleep(0.5)
        os.system("cls")
        Booking = input("Would you like to view our offers? (Yes or No): ").lower()
        if Booking == "yes":
            print(price)
        else:
            pass
    
    #this while loops asks what group you are (Student, Teenager etc) then it shows the prices based on the input.
    #once you select screen type, you can then enter how many tickets you need which will be saved to receipt.
        while True:
            Person = input("\n""Are you a Student, Teenager, Child or Adult (Case sensitive): ")
            if Person == "Student":
                for format, people in price["Student"].items():
                    print(f"{format}: {people}")

                type = input("what screening would you like, 2D, 3D or IMAX (case senstive):")
                if type in price[Person]:
                    print(f"you have selected {type}")
                    with open("reciept.txt", "a") as file:
                        file.write(f"{Person}\nScreen: {type} ")
                    amount = int(input("how many tickets would you like: "))
                    if amount > 0:
                        print(f"you have selected : {amount}")
                        with open("reciept.txt", "a") as file:
                            file.write(f"\nTickets: {amount}")
                        pass
                    else:
                        print("please enter an amount needed.")
                else:
                    print("invalid ticket type")

            elif Person == "Teenager":
                for format, people in price["Teenager"].items():
                    print(f"{format}: {people}")

                type = input("what screening would you like, 2D, 3D or IMAX (case senstive):")
                if type in price[Person]:
                    print(f"you have selected {type}")
                    with open("reciept.txt", "a") as file:
                        file.write(f"{Person}\nScreen: {type}")
                    amount = int(input("how many tickets would you like: "))
                    if amount > 0:
                        print(f"you have selected : {amount}")
                        with open("reciept.txt", "a") as file:
                            file.write(f"\nTickets: {amount}")
                        pass
                else:
                    print("invalid ticket type")

            elif Person == "Child":
                for format, people in price["Child"].items():
                    print(f"{format}: {people}")

                type = input("what screening would you like, 2D, 3D or IMAX (case senstive):")
                if type in price[Person]:
                    print(f"you have selected {type}")
                    with open("reciept.txt", "a") as file:
                        file.write(f"{Person}\nScreen: {type}")
                    amount = int(input("how many tickets would you like: "))
                    if amount > 0:
                        print(f"you have selected : {amount}")
                        with open("reciept.txt", "a") as file:
                            file.write(f"\nTickets: {amount}")
                        pass
                else:
                    print("invalid ticket type")

            elif Person == "Adult":
                for format, people in price["Adult"].items():
                    print(f"{format}: {people}")

                type = input("what screening would you like, 2D, 3D or IMAX (case senstive):")
                if type in price[Person]:
                    print(f"you have selected {type}")
                    with open("reciept.txt", "a") as file:
                        file.write(f"{Person}\nScreen: {type}")
                    amount = int(input("how many tickets would you like: "))
                    if amount > 0:
                        print(f"you have selected : {amount}")
                        with open("reciept.txt", "a") as file:
                            file.write(f"\nTickets: {amount}")
                        pass
                else:
                    print("invalid ticket type")
                    continue
            else:
                print("please select your category.")
                continue
        #this adds up the prices from the person and screen type with added VAT then it also adds it to the receipt    
            YourTotal = price[Person][type] * amount * 1.20
            os.system("cls")
            try:
                print(f"Thank you for your buisness, your total is: {YourTotal}")
                with open("reciept.txt", "a") as file:
                    file.write(f"\nTotal payed: {YourTotal:.2f} \n")
            except FileNotFoundError:
                print("file not found")
        #with the while loop, the user can make more bookings if needed or end their experience
            more = input("would you like more tickets? (Yes or No): ").lower()
            if more != "yes":
                break
    except KeyError:
        print("Wrong input")
        Tickets()
