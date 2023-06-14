"""Validate age input type and value. Loop till correct value is entered"""
while True:
    try:
        age = input("Enter your age: ")
        age = int(age)
    except ValueError:
        print("please enter a numeric digit")
        continue
    except KeyboardInterrupt:
        print("Program terminated")
        break

    if age < 1:
        print("Please enter a positive number")
    break

print(f"You are {age} years old!")
