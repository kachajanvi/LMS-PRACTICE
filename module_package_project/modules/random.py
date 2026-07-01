import random
def random_number():
    a = int(input("Start: "))
    b = int(input("End: "))
    print(random.randint(a,b))

def random_list():
    a = int(input("Start: "))
    b = int(input("End: "))
    n = int(input("Size: "))
    print([random.randint(a,b) for i in range(n)])

def random_password():
    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
    n = int(input("Length"))
    print("".join(random.choice(chars)for i in range(n)))

def random_otp():
    print(random.randint(100000,999999))