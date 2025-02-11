import random
import win32com.client  # Using pywin32 instead of pyttsx3

# Initialize Windows Speech API (SAPI)
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Predefined D&D-style affirmations (heroic encouragements)
affirmations = [
    "The road ahead may be long, but your will is unbreakable.",
    "Even the smallest spark can ignite a great fire within you.",
    "Your strength is not in your sword, but in your heart.",
    "No battle is ever truly lost while hope remains.",
    "The wisdom you seek is already within you—trust in your path.",
    "Even the gods admire your courage today.",
    "The fates weave a grand destiny for you; embrace it.",
    "Your resilience is your greatest weapon in this adventure.",
    "No dungeon is too deep, no mountain too high for a hero like you.",
    "You are not alone—your allies walk beside you in spirit and in strength."
]

hero_class = None  # Store the user's chosen D&D class (e.g., Paladin, Sorcerer)

# Function to display D&D-style ASCII art
def display_banner():
    print(r"""
     █████╗ ███████╗███████╗███████╗███╗   ██╗███████╗
    ██╔══██╗██╔════╝██╔════╝██╔════╝████╗  ██║██╔════╝
    ███████║███████╗███████╗█████╗  ██╔██╗ ██║█████╗  
    ██╔══██║╚════██║╚════██║██╔══╝  ██║╚██╗██║██╔══╝  
    ██║  ██║███████║███████║███████╗██║ ╚████║██║     
    ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝     

        ⚔️ Words of Encouragement for Your Heroic Quest ⚔️
    """)
    print("NOTE: This program plays sounds. Check your volume.\n")

# Function to speak text aloud
def speak(text):
    speaker.Speak(text)

# Function to generate a D&D-style affirmation
def generate_affirmation():
    affirmation = random.choice(affirmations)
    if hero_class:
        affirmation = affirmation.replace("You", f"You, brave {hero_class}")
    print("\n🎲 " + affirmation + "\n")
    speak(affirmation)

# Function to let the user choose a D&D class
def set_hero_class():
    global hero_class
    new_class = input("What is your class, adventurer? (e.g., Paladin, Rogue, Sorcerer) Or, press Enter to clear: ").strip()
    if new_class:
        hero_class = new_class
        print(f"Ah, a {hero_class}! The realm has been waiting for a hero like you.")
        speak(f"Ah, a {hero_class}! The realm has been waiting for a hero like you.")
    else:
        hero_class = None
        print("Class selection cleared. You are now just a wandering traveler.")
        speak("Class selection cleared. You are now just a wandering traveler.")

# Function to provide lore about the "world" (instead of just about the program)
def about_program():
    about_text = "You are a hero on a grand adventure, seeking wisdom and strength. This program offers guidance and encouragement on your journey."
    print("\n📜 " + about_text + "\n")
    speak(about_text)

# Function to handle user commands (D&D-style)
def main():
    display_banner()
    
    while True:
        print("🔮 COMMANDS:")
        print("⚔️ Press Enter to receive a divine prophecy (an affirmation).")
        print("🛡 Type 'class' to choose your adventurer's path.")
        print("📜 Type 'lore' to learn about this realm.")
        print("🚪 Type 'Q' or 'quit' to leave the tavern.")
        
        choice = input("\n[Enter/class/lore/Q]: ").strip().lower()

        if choice == "":
            generate_affirmation()
        elif choice == "class":
            set_hero_class()
        elif choice == "lore":
            about_program()
        elif choice in ["q", "quit"]:
            print("\n🏰 Safe travels, adventurer! The realm awaits your return.\n")
            speak("Safe travels, adventurer! The realm awaits your return.")
            break
        else:
            print("\n⚠️ The scrolls do not recognize this command. Try again, adventurer.\n")
            speak("The scrolls do not recognize this command. Try again.")

# Run the program
main()
