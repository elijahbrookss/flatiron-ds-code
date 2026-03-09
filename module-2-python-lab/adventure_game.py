# List of location names in the order they appear in the menu
# Index 0 corresponds to menu choice 1, index 1 to choice 2, etc.
LOCATIONS = ["Forest", "Cave", "Beach"]

# Dictionary containing the story text for each location
# The key is the location name and the value is a list of lines to print
# N. K. Jemisin style .. ifykyk
TEXTS = {
    "Forest": [
        "The trees are older than the name anyone gave them. They don't mind that you're here.",
        "Light filters down in long, slow columns. Something watches - not with malice, just attention.",
        "You get the sense the forest has seen many people pass through. It is still deciding what you are.",
    ],
    "Cave": [
        "The dark here isn't empty. It has weight, and it settles around you like a second skin.",
        "Your footsteps echo longer than they should. The cave is considering your presence.",
        "There is something further in. You don't have to go - but you already know you will.",
    ],
    "Beach": [
        "The shore is quiet in the way that means something recently left, or is about to arrive.",
        "The water doesn't look right, but you can't say why. You stand at the edge anyway.",
        "The horizon holds your gaze a little too long. You file that away for later.",
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