#fundamental booster
print("welcom to interactive personal data cpllection python")

name=input(input("please enter your name:"))
age=int(input("please enter your age:"))
height=float(input("please enter your height:"))
favourite=int(input("please enter your favorite number:"))

print("\nthank you!for your information.")
print("here is your information we collect")
print("\n")
print(f"name:{name}(type:{type(name)},memory address:{id(name)}")
print(f"age: {age}(type:{type(age)},memory address:{id(age)}")
print(f"heigh:{height}(type:{type(height)},memory address:{id(height)})")
print("ffavorite:{favourite}(type:{type(favourite)},memory address:{id(favourite)})")

birth_year=2026 - age

print(f"your birth year is approximately ({birth_year}(based on your age{age}))")
print("/n")
print("thank you for using the personal data collecter.goodbyee!")
      
