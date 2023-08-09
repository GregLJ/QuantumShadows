# Author: Gregory John

import copy


class QuantumShadowsGame:
    def __init__(self):
        self.inventory = []
        self.boss = 'Nexus Nocturn, The Quantum Sorcerer'
        self.codex_fragments = ['Stellar Sand', 'Chrono Crystal', 'Fragment of Continuum',
                                'Mirror Shard', 'Abyssal Echo', 'Paradox Leaf']
        self.initialize_dimensions()

    def initialize_dimensions(self):
        self.dimensions = {
            'Chronomoria Courtyard': {'North': "Astral Atoll", 'Item': None},
            'Astral Atoll': {'South': 'Chronomoria Courtyard', 'North': 'Quantum Crypt',
                             'East': "Temporal Tundra", 'Item': self.codex_fragments[0]},
            'Quantum Crypt': {'South': 'Astral Atoll', 'Item': self.boss},
            'Temporal Tundra': {'West': 'Astral Atoll', 'South': 'Solar Sanctuary',
                                'Item': self.codex_fragments[1]},
            'Solar Sanctuary': {'North': 'Temporal Tundra', 'South': 'Glass Labyrinth',
                                'East': 'Echoing Abyss', 'Item': self.codex_fragments[2]},
            'Glass Labyrinth': {'North': 'Solar Sanctuary', 'Item': self.codex_fragments[3]},
            'Echoing Abyss': {'West': 'Solar Sanctuary', 'North': 'Clockwork Jungle',
                              'Item': self.codex_fragments[4]},
            'Clockwork Jungle': {'South': 'Echoing Abyss', 'Item': self.codex_fragments[5]}
        }

    def show_instructions(self):
        print('Quantum Shadows')
        print('The Quantum Sorcerer, Nexus Nocturn, is tearing holes in reality, creating interdimensional portals.')
        print('Your objective is to move through these portals and collect the 6 fragments of the Quantum Codex')
        print('and strip Nexus Nocturne of his powers once and for all.')
        print('Movement commands: go North, go South, go East, go West')
        print('Add items to your inventory: get "item_name"')
        print('Lets Begin!')
        print()

    def reset_game(self):
        print("\nTime and space collapse around you, and everything starts anew...\n")
        self.initialize_dimensions()
        self.inventory.clear()
        return self.show_status('Chronomoria Courtyard')

    def show_status(self, current_room):
        # If in the Quantum Crypt room and boss is present, check if player has all items
        if current_room == 'Quantum Crypt' and self.dimensions[current_room].get('Item') == self.boss:
            if set(self.codex_fragments).issubset(set(self.inventory)):
                print("\nAs you step into the Quantum Crypt, the 6 fragments of the Quantum Codex emanate an unmatched "
                      "power.")
                print(f"You confront {self.boss} with the codex's energy and time and space begin to heal!")
                print("The fractures are restoring, bringing normal order. Congratulations, you've saved reality!")
                return 'exit'  # End the game
            else:
                print("\nYou come face-to-face with Nexus Nocturn, The Quantum Sorcerer!")
                print(
                    "Without all the fragments of the Quantum Codex, reality gets torn apart and time and space reset!")
                print("Try to collect all the fragments before facing Nexus Nocturn next time.")
                print("\nReality is resetting...")
                return self.reset_game()
        # Print the current room
        print("You are currently in the", current_room)
        # Check if there's an item in the room
        # Check if there's an item in the room
        item_in_room = self.dimensions[current_room].get('Item')
        if item_in_room:
            if item_in_room in self.inventory:
                print("You search the area and find that you've already taken the", item_in_room)
            else:
                print("You search the area and find the", item_in_room)
        else:
            print("You search the area and find nothing of note.")
        # Show player's inventory
        print("Inventory:", ', '.join(self.inventory) if self.inventory else "empty")
        print("----------------------------")
        return current_room  # Continue with the current room

    def move(self, direction, current_room):
        direction = direction.title()
        if direction in self.dimensions[current_room]:
            current_room = self.dimensions[current_room][direction]
            print("You are now in the", current_room)
            print()
        else:
            print("You cannot move in that direction.")
        return current_room  # Ensure a valid room is always returned


    def get_item(self, item_to_get, current_room):
        """Attempt to get the item specified by the player."""
        # Convert player's input and stored item name to lowercase for case-insensitive comparison
        item_to_get_lower = item_to_get.lower()
        stored_item_lower = self.dimensions[current_room].get('Item', '').lower()

        if 'Item' in self.dimensions[current_room] and stored_item_lower == item_to_get_lower:
            print(f'You have picked up {self.dimensions[current_room]["Item"]}!')
            self.inventory.append(self.dimensions[current_room]['Item'])
            self.dimensions[current_room]['Item'] = None
        else:
            print(f'There is no {item_to_get} here.')


    def print_options(self, current_room):
        """Print available options to the player."""
        print("What would you like to do?")
        print("To move, type go followed by the direction you want to go in: ",
              ', '.join([dir for dir in self.dimensions[current_room].keys() if dir != 'Item']))
        print("To pick up an item, type: get 'item_name'")
        print("To exit the game, type: exit")


    def handle_command(self, command, current_room):
        action = command[0].lower()
        if not current_room:  # If current_room is None, just return it without processing any action
            print("There seems to be a rift in time. Please try moving.")
            return current_room
        if action == 'go':
            if len(command) < 2:
                print("You need to specify a direction to go. Please try again.")
                return current_room
            return self.move(' '.join(command[1:]), current_room)
        elif action == 'get':
            item_to_get = ' '.join(command[1:])
            self.get_item(item_to_get, current_room)
            return current_room  # Return the current room unchanged
        elif action == 'exit':
            return 'exit'
        else:
            print("I'm not sure what you mean by that. Please use one of the specified commands.")
            return current_room


    def play(self):
        self.show_instructions()
        current_room = 'Chronomoria Courtyard'

        while current_room != 'exit':
            current_room = self.show_status(current_room)
            if current_room == 'exit':
                break

            self.print_options(current_room)
            command = input().split()

            if not command:  # Handling empty input
                print("Sorry, I didn't catch that. Please try again.")
                continue

            current_room = self.handle_command(command, current_room)

        print("Thank you for playing!")


# To play the game:
game = QuantumShadowsGame()
game.play()
