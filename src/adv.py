from room import Room
from player import Player 

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

inits = 'Start Game'
location = 'Outside'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Travis', room['outside'])
current_room = player.current_room
print(current_room)

# Create function for player movement in any direction
def command(p_inpt):
    '''
    This function will handle all player movement in any direction (n, s, e, w).
    q will equate to quitting.
    '''

# Move player
# global current_room
if p_inpt[0] == 'n':
     if hasattr(current_room, "n_to"):
            new_room = current_room.n_to
            current_room = new_room
            print(
                f"You are now at the {current_room.name}. {current_room.description}.")
elif p_inpt[0] == 's':
    if hasattr(current_room, 's_to'):
        new_room = current_room.s_to
        current_room = new_room
        print(
            f"You are now at the {current_room.name}. {current_room.description}")
elif p_inpt[0] == 'e':
    if hasattr(current_room, 'e_to'):
        new_room = current_room.e_to
        current_room = new_room
        print(
            f"You are now at the {current_room.name}. {current_room.description}")
elif p_inpt[0] == 'w':
    if hasattr(current_room, 'w_to'):
        new_room = current_room.w_to
        current_room = new_room
        print(
            f"You are now at the {current_room.name}. {current_room.description}")

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

print(
    f"\n Welcome to your first adventure, {player.name}! \n Use 'n' to go North \n Use 's' to go South \n Use 'w' to go West \n Use 'e' to go East \n Press 'q' to quit game")

while not inits[0] == 'q':
    if current_room == room['outside']:
        print(f'You are currently {current_room}\n')
    else:
        print('\nERROR: NOT ALLOWED \n')

    try:
        inits = input('Enter a command: \n')
        command(inits)
    except AttributeError:
        print("Unavailable\n")
        continue

if p_inpt[0] == 'q':
    print('Exiting game. See you next time! \n')
