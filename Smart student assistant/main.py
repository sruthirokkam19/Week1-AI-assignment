import json
import random
from datetime import datetime

# Ask user name
name = input("Enter your name: ")

print(f"\nHello {name}! Welcome to Smart Student Assistant")

# Load JSON data
with open("tips.json", "r") as file:
    data = json.load(file)

while True:
    print("\n===== MENU =====")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    result = ""

    if choice == "1":
        result = random.choice(data["study_tips"])
        print("\nStudy Tip:")
        print(result)

    elif choice == "2":
        result = random.choice(data["quotes"])
        print("\nMotivation Quote:")
        print(result)

    elif choice == "3":
        result = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print("\nCurrent Date & Time:")
        print(result)

    elif choice == "4":
        print("Thank you for using Smart Student Assistant!")
        break

    else:
        print("Invalid choice!")
        continue

    # Save output to text file
    with open("output.txt", "a") as file:
        file.write(result + "\n")
