from datetime import datetime

class journal:
    def add_entry(self): 
        filename = input("Enter file name:")
        entry = input("Enter journal entry:")

        time = datetime.now().strftime("%d-%m-%Y %H%M%S")

        with open(filename, "a") as file:
            file.write(f"[{time}] {entry}\n")

        print("Entry added successfully!") 

    def view_entries(self):
        filename = input("Enter file name:")

        try:
            with open(filename, "r") as file:
                print("\n-----Journal Entries-----")
                print(file.read())

        except FileNotFoundError:
            print("File not found!")

    def delete_entries(self):
        filename = input("Enter file name:")
        confirm = input("Delete all entries? (yes/no)")

        if confirm.lower() == "yes":
            open(filename, "w").close()
            print("ALL entries deleted!")
        else:
            print("Delete cancelled.")

    def menu(self):
        while True:
            print("\n=====Journal Manager=====")
            print("1.Add Entry")
            print("2.View Entries")
            print("3.Delete Entries")
            print("4.Exit")

            choice = input("Enter your choice:")

            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.view_entries()
            elif choice == "3":
                self.delete_entries()
            elif choice == "4":
                print("Program Ended.")
                break
            else:
                print("Invalid choice!")

obj = journal()
obj.menu()
        
    
