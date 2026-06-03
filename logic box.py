#logic box

while True:
    print("welcome to the pattern generator and numbers analyzer!")
    print("1.genrate a pattern")
    print("2.analyze a range of numbers")
    print("3.exit")

    choice = input("enter your choice:")

    if choice == "1":
        while True:
            print("choose a pattern type")
            print("1.right-angle triangle")
            print("3.left-right triangle")

            pattern_choice = input("enter your choice:")

            rows = int(input("enter your choice:"))

            print("\n pattern:")

            if pattern_choice == "1":

                #right-angle triangle
                for i in range(1, rows + 1):
                    print("*" * i)

            elif pattern_choice == "2":

                        #pyramid
                        for i in range(1, rows + 1):
                            print(" " * (rows-1) , end=" ")

                            print("*" * (2 * i - 1))

            elif pattern_choice == "3":

                                #left-angle triangle
                                for i in range(1,rows + 1):
                                    print(" " * (rows-1) + "*" * i)

            elif choice =="2":

                                        start = int(input("enter start number:"))
                                        end + int(input("enter end number:"))

                                        total = 0
                                        print()

                                        for num in range(start, end+1):
                                            if num%2==0:
                                                print(num, "is even")
                                            else:
                                                print(num, "is odd")

                                                total=total + num

                                                print("\n sum = " , total)

            elif choice == "3":
                                                    print("program end")
            else:
                                                    print("invalid choice")
                
