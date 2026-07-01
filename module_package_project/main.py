from modules import Date
from modules import file
from modules import random
from modules import maths
from modules import uuid

def date_menu():
    while True:
        print("\n====== Date & Time Menu ========")
        print("1.Current Date & Time")
        print("2.Date Different")
        print("3.Format Date")
        print("4.Stopwatch")
        print("5.Countdown")
        print("6.Exit")

        choice = int(input("Enter choice: "))

        if choice == 1 :
            Date.display_current_datetime()
        elif choice == 2 :
            Date.date_difference()
        elif choice == 3 :
            Date.format_date()
        elif choice == 4 :
            Date.stopwatch()
        elif choice == 5 :
            Date.countdown_timer()
        elif choice == 6:
            print("Thank You!")
            break
        else:
            print("Invalid choice")


def File_menu():
    while True:
        print("\n------------file operations-------------")
        print("1.create file")
        print("2.view file")
        print("3.search file")
        print("4.delete file")
        print("5.Back")

        choice = int(input("Enter your choice: "))

        if choice == 1 :
            file.create()
        elif choice == 2 :
            file.view()
        elif choice == 3 :
            file.search()
        elif choice == 4 :
            file.delete()
        elif choice == 5 :
            break
        else:
            print("Invalid choice")


def random_menu():
    while True:
        print("\n----------Random Operations-------")
        print("1.Random Number")
        print("2.Random List")
        print("3.Random Password")
        print("4.Random OTP")
        print("5.Back")

        choice = int(input("Enter your choice: "))

        if choice == 1 :
            random.random_number()
        elif choice == 2 :
            random.random_list()
        elif choice == 3 :
            random.random_password()
        elif choice == 4 :
            random.random_otp()
        elif choice == 5 :
            break
        else:
            print("Invalid choice.please try again")


def maths_menu():
    while True:
        print("\n---------Math Operations----------")
        print("1.Factorial")
        print("2.Interest Calculator")
        print("3.1Trigonometric Calculator")
        print("4.Geometry Calculator")
        print("5.Back")

        choice = int(input("Enter your choice: "))

        if choice == 1 :
            maths.factorial()
        elif choice == 2 :
            maths.interest()
        elif choice == 3 :
            maths.trig()
        elif choice == 4 :
            maths.geometry()
        elif choice == 5 :
            break 
        else:
            print("Invalid choice")
             
def UUID_menu():
    while True:
        print("\n======= UUID Menu =========")
        print("1.Generate UUID")
        print("2.Back")

        choice = int(input("Enter choice: "))

        if choice == 1 :
            uuid.generate_uuid()
        elif choice == 2 :
            print("Thank You!")
            break
        else:
            print("Invalid choice")

def main():
    while True:
        print("\n====== Main Menu ========")
        print("1.Date & Time")
        print("2.File")
        print("3.Random")
        print("4.Maths")
        print("5.UUID")
        print("6.Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1 :
            date_menu()
        elif choice == 2 :
            File_menu()
        elif choice == 3 :
            random_menu()
        elif choice == 4 :
            maths_menu()
        elif choice == 5 :
            UUID_menu()
        elif choice == 6 :
            print("Thank You!")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
