# Author: Gregory John

# Define movement direction constants for clarity
NORTH, SOUTH, EAST, WEST = 'North', 'South', 'East', 'West'
DIRECTIONS = (NORTH, SOUTH, EAST, WEST)  # Grouping all directions for validation purposes

# Define dimension room constants for clarity and to prevent typos
# Each of these represents a specific room in the game.
CHRONOMORIA_COURTYARD, ASTRAL_ATOLL, QUANTUM_CRYPT, TEMPORAL_TUNDRA, SOLAR_SANCTUARY, \
GLASS_LABYRINTH, ECHOING_ABYSS, CLOCKWORK_JUNGLE = (
    'Chronomoria Courtyard', 'Astral Atoll', 'Quantum Crypt', 'Temporal Tundra',
    'Solar Sanctuary', 'Glass Labyrinth', 'Echoing Abyss', 'Clockwork Jungle'
)
# Define the main antagonist of the game
BOSS = 'Nexus Nocturn, The Quantum Sorcerer'


def show_instructions():
    """Displays the game's instructions to guide the player."""
    instructions = [
        'Quantum Shadows\n',
        'The Quantum Sorcerer, Nexus Nocturn, weaves fractures in the fabric of reality, conjuring interdimensional rifts.',
        'You are chosen by fate to journey these rifts, seeking the 6 fragments of the Quantum Codex.',
        'Gather these fragments to seal the sorcerer\'s power, and restore balance to the dimensions.',
        'To navigate the dimensions: voice a direction such as "go North, go South, go East, go West".',
        'To claim relics on your journey: utter "get \'item_name\'".',
        'Awaken, traveler, and may the Quantum Codex guide you!\n'
    ]
    print('\n'.join(instructions))


class QuantumShadowsGame:
    """Main class that handles the game mechanics."""
    def __init__(self):
        """Constructor to initialize the game's initial state."""
        self._previous_room = None  # Keeps track of the last room the player was in (for backtracking purposes)
        self.dimensions = None  # This will hold the map structure of our game.
        self._current_room = CHRONOMORIA_COURTYARD  # Start the player in the courtyard
        self._inventory = []  # This is the player's "bag". It will hold items they pick up.
        self._boss = BOSS  # Defines the main antagonist
        # Fragments that players need to collect before confronting the boss
        self._codex_fragments = ['Stellar Sand', 'Chrono Crystal', 'Fragment of Continuum',
                                 'Mirror Shard', 'Abyssal Echo', 'Paradox Leaf']
        # Descriptions for each room to paint a picture for the player.
        self.room_descriptions = {
            CHRONOMORIA_COURTYARD: "The gateway to the dimensions. It's eerily quiet, as though time itself has paused.",
            ASTRAL_ATOLL: "You find yourself on an island floating amidst a vast astral sea. Stars twinkle beneath your feet.",
            QUANTUM_CRYPT: "Darkness envelopes this realm, pierced only by the sorcerer's haunting aura.",
            TEMPORAL_TUNDRA: "Chilled winds brush past as you observe the glacial expanse. Snowflakes hang motionless in the air.",
            SOLAR_SANCTUARY: "The gentle hues of an eternal sunset paint the walls of this serene cathedral.",
            GLASS_LABYRINTH: "Endless reflections confront you, each mirror revealing a reality slightly different than the last.",
            ECHOING_ABYSS: "The void stretches endlessly. Every footstep echoes, painting unseen landscapes with sound.",
            CLOCKWORK_JUNGLE: "Gears whir and steam hisses from the mechanical flora. Metallic birds take flight with clockwork precision."
        }
        self.initialize_dimensions()  # Call method to initialize the game's dimensions

    @property
    def current_room(self):
        """Return the current room. Using a property allows controlled access."""
        return self._current_room

    @property
    def inventory(self):
        """Return the player's inventory. Using a property provides controlled access."""
        return self._inventory

    def initialize_dimensions(self):
        """Set up the initial map structure of the game with available directions and items in each room."""
        # Dictionary structure allows for easy lookup of directions and items for each room.
        self.dimensions = {
            CHRONOMORIA_COURTYARD: {'directions': {NORTH: ASTRAL_ATOLL}, 'item': None},
            ASTRAL_ATOLL: {'directions': {SOUTH: CHRONOMORIA_COURTYARD, NORTH: QUANTUM_CRYPT, EAST: TEMPORAL_TUNDRA},
                           'item': self._codex_fragments[0]},
            QUANTUM_CRYPT: {'directions': {SOUTH: ASTRAL_ATOLL}, 'item': self._boss},
            TEMPORAL_TUNDRA: {'directions': {WEST: ASTRAL_ATOLL, SOUTH: SOLAR_SANCTUARY},
                              'item': self._codex_fragments[1]},
            SOLAR_SANCTUARY: {'directions': {NORTH: TEMPORAL_TUNDRA, SOUTH: GLASS_LABYRINTH, EAST: ECHOING_ABYSS},
                              'item': self._codex_fragments[2]},
            GLASS_LABYRINTH: {'directions': {NORTH: SOLAR_SANCTUARY}, 'item': self._codex_fragments[3]},
            ECHOING_ABYSS: {'directions': {WEST: SOLAR_SANCTUARY, NORTH: CLOCKWORK_JUNGLE},
                            'item': self._codex_fragments[4]},
            CLOCKWORK_JUNGLE: {'directions': {SOUTH: ECHOING_ABYSS}, 'item': self._codex_fragments[5]}
        }

    def reset_game(self):
        """Resets the game to its initial state."""
        print("\nTime and space collapse around you, and everything starts anew...\n")
        self.initialize_dimensions()
        self.inventory.clear()
        return CHRONOMORIA_COURTYARD  # Start in the courtyard

    def show_status(self, current_room):
        """Displays the current status of the player and checks for game-ending conditions."""
        # If in the Quantum Crypt room and boss is present, check if player has all items
        if current_room == QUANTUM_CRYPT and self.dimensions[current_room]['item'] == self._boss:
            print("You come face-to-face with Nexus Nocturn, The Quantum Sorcerer!")
            if set(self._codex_fragments).issubset(set(self._inventory)):
                print(
                    "\nAs you step further into the Quantum Crypt, the 6 fragments of the Quantum Codex emanate an "
                    "unmatched power.")
                print(f"You confront {self._boss} with the codex's energy and time and space begin to heal!")
                print("The fractures are restoring, bringing normal order. Congratulations, you've saved reality!")
                return 'exit'  # End the game
            else:
                choice = input(
                    "Do you want to confront the boss without the fragments or flee to the previous room? ("
                    "confront/flee): ")
                if choice.lower() == "confront":
                    print(
                        "Without all the fragments of the Quantum Codex, reality gets torn apart and time and space "
                        "reset!")
                    print("Try to collect all the fragments before facing Nexus Nocturn next time.")
                    print("\nReality is resetting...")
                    return self.reset_game()
                elif choice.lower() == "flee":
                    print("You decide to flee back to the safety of the previous dimension.")
                    current_room = self._previous_room
                    return self.show_status(current_room)
                else:
                    print("Unsure of what to do, you hesitate, and time and space collapse around you!")
                    return self.reset_game()

        # Print the current room
        print(f"You find yourself within the {current_room}, a dimension distorted by Nexus Nocturn's magic.")
        print(self.room_descriptions[current_room])
        # Check if there's an item in the room
        item_in_room = self.dimensions[current_room]['item']
        if item_in_room:
            print(f"Whispers of the Quantum Codex guide you towards the {item_in_room}.")
            if item_in_room in self._inventory:
                print(f"You recall the energy; you've already claimed the {item_in_room} in a past traversal.")
        else:
            print("The dimension seems barren; no fragments of the Codex resonate here.")
        # Show player's inventory
        if self._inventory:
            relics = ', '.join(self._inventory)
            print(f"The fragments you've gathered resonate within your satchel: {relics}.")
        else:
            print("Your satchel remains empty; the Quantum Codex is yet to be reformed.")
        print("-" * 80)
        return current_room  # Continue with the current room

    def move(self, direction, current_room):
        """Move the player in the given direction."""
        direction = direction.title()
        self._previous_room = current_room
        if direction in self.dimensions[current_room]['directions']:
            print("\nA rift shimmers into existence. You step through, your senses shifting as the dimension alters.")
            print()
            # Update the current room based on the direction chosen by the player.
            self._current_room = self.dimensions[current_room]['directions'][direction]
            return self._current_room  # Return the updated current room
        else:
            print(f"An attempt to weave a rift to the {direction} shatters. This path remains elusive in this realm.")
        return current_room  # If direction is invalid, return the original room

    def get_item(self, item_to_get, current_room):
        """Adds an item to the player's inventory."""
        item_to_get = ' '.join([word.title() if word not in ['of', 'and', 'or', 'the', 'a', 'an']
                                else word for word in item_to_get.strip().split()])
        if self.dimensions[current_room]['item'] == item_to_get:
            print(f"The energies of {self.dimensions[current_room]['item']} now resonate within you.")
            self.inventory.append(self.dimensions[current_room]['item'])
            self.dimensions[current_room]['item'] = None
        else:
            print(f"'{item_to_get}' remains but a whisper in this realm. Seek that which vibrates with the realm's energy.")

    def print_options(self, current_room):
        """Print available options to the player."""
        print("What would you like to do?")
        available_dirs = list(self.dimensions[current_room]['directions'].keys())
        print(f"To tread a new path, utter 'go' and then the direction of your choice: {', '.join(available_dirs)}")
        print("To pick up an item, type: get 'item_name'")
        print("To exit the game, type: exit")

    def handle_command(self, user_input, current_room):
        """Handles player's input, interprets the commands and performs game actions."""
        user_input = user_input.lower().strip()
        # Split the user input to interpret commands like 'go north' or 'get item'.
        tokens = user_input.split(' ')

        # Check if user wants to move.
        if tokens[0] == 'go':
            if len(tokens) > 1:
                direction = tokens[1]
                if direction.title() in DIRECTIONS:
                    current_room = self.move(direction, current_room)
                else:
                    print(f"The energies of '{direction}' do not resonate in this dimension. Seek a familiar path.")
            else:
                print("The paths of the dimensions are mysterious. Which direction do you wish to tread? (e.g., 'go north').")

        # Check if user wants to pick up an item.
        elif tokens[0] == 'get':
            if len(tokens) > 1:
                item_to_get = ' '.join(tokens[1:])
                self.get_item(item_to_get, current_room)
            else:
                print("Please specify an item to pick up (e.g., 'get item_name').")

        # Allow the user to exit the game.
        elif user_input == 'exit':
            print("You've decided to abandon your quest, time and space are in disarray. Farewell, traveler.")
            return 'exit'
        else:
            print(f"'{user_input}' is not of this realm. Seek clarity, and the dimensions shall respond.")
        return current_room

    def play(self):
        """Main game loop that orchestrates the game's flow."""
        show_instructions()  # Display game instructions at the start
        current_room = CHRONOMORIA_COURTYARD  # Start in the courtyard
        game_over = False

        while not game_over:  # Continue running the game until the exit condition is met
            current_room = self.show_status(current_room)  # Display the current status to the player
            if current_room == 'exit':  # If the status method returns 'exit', end the game
                game_over = True
                continue
            self.print_options(current_room)  # Show available options to the player
            user_input = input()  # Take input from the player for their next move
            current_room = self.handle_command(user_input, current_room)  # Handle the player's input
            if current_room == 'exit':  # Check for exit condition again after handling input
                game_over = True


# This condition ensures the game runs only when this script is executed directly and not imported elsewhere.
if __name__ == '__main__':
    game_instance = QuantumShadowsGame()  # Create an instance of the game
    game_instance.play()  # Begin the game!
