def module():
    name = input("Enter module name: ")
    mod = __import__(name)
    print(dir(mod))