# List of location names in the order they appear in the menu
# Index 0 corresponds to menu choice 1, index 1 to choice 2, etc.
LOCATIONS = ["Forest", "Cave", "Beach"]

# Dictionary containing the story text for each location
# The key is the location name and the value is a list of lines to print
TEXTS = {
    "Forest": [
        "Tall trees surround you, filtering sunlight into golden beams.",
        "The quiet here feels wise. You breathe deeply and think clearly.",
        "Sometimes the best answers come from slowing down.",
    ],
    "Cave": [
        "It is dark, and the air smells of damp stone and old secrets.",
        "Your torch flickers, but just ahead... something glimmers.",
        "Risk brought you here. Courage will take you further.",
    ],
    "Beach": [
        "Waves roll in steadily, one after another, never stopping.",
        "You sit on the sand and look out at the horizon.",
        "The ocean reminds you.. plan your path, then take the first step.",
    ],
}

def show_menu():
    print("\nWelcome to the Adventure Game")
    print("Where would you like to go?")

    # enumerate() is used to number each location starting from 1
    # This keeps the menu numbers aligned with the LOCATIONS list
    for i, name in enumerate(LOCATIONS, start=1):
        print(f"  {i} = {name}")

def play_game():
    while True:
        # Show the menu options each time the loop runs
        show_menu()

        # Ask the user for input
        user_input = input(f"Enter 1 to {len(LOCATIONS)}: ")

        try:
            # Convert the input to an integer
            choice = int(user_input)

            # Validate that the number is within the valid range
            if choice < 1 or choice > len(LOCATIONS):
                print(f"\nThat is not a valid choice. Please enter 1 to {len(LOCATIONS)}.")
                continue

            # Convert the menu number to the correct list index
            location = LOCATIONS[choice - 1]

        except ValueError:
            # This block runs if the user enters something
            # that cannot be converted to an integer (like text)
            print(f"\nThat is not a valid choice. Please enter 1 to {len(LOCATIONS)}.")
            continue

        # Display the location the player chose
        print(f"\nYou arrive at the {location}.")

        # Print each line of story text associated with that location
        for line in TEXTS[location]:
            print(line)

        # Ask if the player wants to explore again
        again = input("\nExplore again? (yes / no): ").strip().lower()

        # If the player enters anything other than "yes",
        # the game ends and the loop stops
        if again != "yes":
            print("\nThank you for adventuring. Safe travels!")
            break

# Start the game by calling the play_game function
play_game()