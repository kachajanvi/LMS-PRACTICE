from datetime import datetime
import time

def display_current_datetime():
    now = datetime.now()
    print("Date:", now.strftime("%d-%m-%Y"))
    print("Time:", now.strftime("%H:%M:%S"))

def date_difference():
    d1 = datetime.strptime(input("First date (YYYY-MM-DD): "), "%Y-%m-%d")
    d2 = datetime.strptime(input("Second date (YYYY-MM-DD): "), "%Y-%m-%d")
    print("Difference:", (d2 - d1).days, "days")

def format_date():
    d = datetime.strptime(input("Enter date (YYYY-MM-DD): "), "%Y-%m-%d")
    print("formatted:", d.strftime("%d-%m-%Y"))

def stopwatch():
    input("Press Enter to start......")
    start = time.time()
    input("Press Enter to stop........")
    print("Time:", round(time.time() - start, 2), "second")

def countdown_timer():
    sec = int(input("Enter seconds: "))
    while sec:
        print(sec)
        time.sleep(1)
        sec -= 1
    print("Time's up!")