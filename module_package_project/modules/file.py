def write():
    try:
        f = input("File name: ")
        c = input("Content: ")
        with open("Data/" + f, "w")as file:
            file.write(c)
        print("Written Successfully")
    
    except Exception as e:
        print(e)

def create():
    try:
        f = input("File name: ")
        with open("Data/" + f,"a") as file:
            pass
        print("File Created")

    except Exception as e:
        print(e)

def view():
    try:
        f = input("File name: ")
        with open("Data/" + f, "r")as file:
            print(file.read())
        

    except Exception as e:
        print(e)

def search():
    try:
        f = input("File name: ")
        w =input("Search: ")
        with open("Data/" + f, "r")as file:
             print("Found" if w in file.read() else "Not Found")
       
    except Exception as e:
        print(e)

def delete():
    try:
        f = input("File name: ")
        if input("Deleted? (yes/no):").lower == "yes":
            with open("Data/" + f , "w")as file:
                pass
            print("Deleted")
        else:
            print("Cancelled")
    
    except Exception as e:
        print(e)