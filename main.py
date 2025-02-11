import random

# Predefined affirmations list
affirmations = [
    "You are capable of amazing things.",
    "Believe in yourself and your abilities.",
    "Your potential is limitless.",
    "Every day is a fresh start.",
    "You are stronger than you think.",
    "Your hard work will pay off."
]

# Function to generate a random affirmation
def generate_affirmation():
    print("\n✨ Affirmation: " + random.choice(affirmations) + "\n")

# Function to add a new affirmation
def add_affirmation():
    new_affirmation = input("Enter a new affirmation: ")
    affirmations.append(new_affirmation)
    print("\n✅ Your affirmation has been added!\n")

# Function to view all affirmations
def view_affirmations():
    print("\n📜 Saved Affirmations:")
    for idx, affirmation in enumerate(affirmations, start=1):
        print(f"{idx}. {affirmation}")
    print("\n")

# Function to display the main menu and handle user input
def main():
    while True:
        print("\n📝 Affurmations - Words of Encouragement\n")
        print("1️⃣ Generate an Affirmation")
        print("2️⃣ Add an Affirmation")
        print("3️⃣ View All Affirmations")
        print("4️⃣ Quit")

        choice = input("\n🔹 Enter a number: ")

        if choice == "1":
            generate_affirmation()
        elif choice == "2":
            add_affirmation()
        elif choice == "3":
            view_affirmations()
        elif choice == "4":
            confirm = input("⚠️ Are you sure you want to quit? (yes/no): ")
            if confirm.lower() == "yes":
                print("\n👋 Goodbye!\n")
                break
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.\n")

# Run the program
main()
