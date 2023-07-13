# Author: Gregory John

def show_instructions():
    print('Quantum Shadows')
    print('The Quantum Sorcerer, Nexus Nocturn, is tearing holes in reality, creating interdimensional portals.')
    print('Your objective is to move through these portals and collect the 6 fragments of the Quantum Codex')
    print('and strip Nexus Nocturne of his powers once and for all.')
    print('Movement commands: go North, go South, go East, go West')
    print('Add items to your inventory: get "item_name"')


def show_status(currentRoom, inventory, room):
    pass


def main():
    dimensions = {
        'Chronomoria Courtyard': {'North': "Astral Atoll", 'Item': "Stellar Sand"},
        'Astral Atoll': {'South': 'Chronomoria Courtyard', 'North': 'Quantum Crypt', 'East': "Temporal Tundra",
                         'Item': 'Stellar Sand'},
        'Quantum Crypt': {'South': 'Astral Atoll', 'Item': 'Nexus Nocturn, The Quantum Sorcerer'},
        'Temporal Tundra': {'West': 'Astral Atoll', 'South': 'Solar Sanctuary', 'Item': 'Chrono Crystal'},
        'Solar Sanctuary': {'North': 'Temporal Tundra', 'South': 'Glass Labyrinth', 'East': 'Echoing Abyss',
                            'Item': 'Fragment of Continuum'},
        'Glass Labyrinth': {'North': 'Solar Sanctuary', 'Item': 'Mirror Shard'},
        'Echoing Abyss': {'West': 'Solar Sanctuary', 'North': 'Clockwork Jungle', 'Item': 'Abyssal Echo'},
        'Clockwork Jungle': {'South': 'Echoing Abyss', 'Item': 'Paradox Leaf'}
    }

    show_instructions()


main()
