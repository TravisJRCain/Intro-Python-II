from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# adding items to game

dagger = Item('dagger', 'A used dagger...')
potion = Item('potion', 'For healing purposes...')

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
       

#
# If the user enters "q", quit the game.
player = Player("Travis", room['outside'])
player.items = [dagger, potion]

# test to see if class is working properly
print(player.items)


quit = False

while not quit:
    player_input = input('Ready to begin your adventure?: ').lower()
    if player_input == 'list':
        print('The following items are in this room: \n')
        for item in player.currentRoom.items:
            print(f'{item.name}: {item.description}')
    cmd = input("Enter a direction:\nEast\nWest\nNorth\nSouth\nor quit----\n")
    cmd = cmd.lower().strip()[0]
    if cmd == 'n' or cmd == 'e' or cmd == 'w' or cmd == 's':
        print(player.move(cmd))
    elif cmd == 'q':
        quit = True
        print('Game Over')
    else:
        print('Enter a valid direction')

print('See you next time!')