#collection mainipulator

print("welcom to interactive personal data collection program")

name=input(input("please enter your name:"))
age=input(input("please enter your age:"))
height=float(input("please enter your height:"))
favourite=int(input("please enter your favourite number:"))

print("\nthank you! for your information.")
print("here is your information we collect")
print("\n")
print(f"name: {name}(type: {type(name)}, memory address: {id(name)})")
print(f"age: {age}(type: {type(age)}, memory address: {id(age)}")
print(f"height: {height}(type: {type(height)}, memory address: {id(height)})")
print(f"favourite: {favourite}(type: {type(favourite)}, memory address: {id(favorite)})")


birth_year=2026 - age

print(f"your birth year is approximately ({birth_year}(based on your age{age}))")
print("/n")
print("thank you for using the personal data collector. goodbyee!")
