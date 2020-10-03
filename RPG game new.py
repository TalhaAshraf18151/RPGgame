#!/bin/python3

def opening_screen():
    # print a main menu and the commands
    print('''
RPG Game
========

Get to the Garden with a key and a potion
Avoid the monsters!

Commands:
  move [direction] directions: north, south, east, west 
  get [item]
''')

def help_screen():
    print('''
    Get to the Garden with a key and a potion
    Avoid the monsters!

Commands:
  move [direction] direction: north, south, east, west 
  get [item]
    '''


    )

def Status():
    # print the player's current status
    print(currentRoom)
    # print the current inventory

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other room positions
rooms = {

    'Spawn room': {'north': 'room1',
             'east': 'room4'
             },

    'room1': {'south': 'Spawn room',
                'east': 'room2',
              'west': 'room3'
                },

    'room2': {'west': 'room1',
                    'south': 'room4'

                    },

    'room3': {'east': 'room1'},

    'room4': {'north': 'room2',
              'west': 'spawn'}

}






# start the player in the Hall
currentRoom = 'Spawn room'

opening_screen()

# loop forever
while True:

    Status()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    go = ''
    while go == '':
        go = input('>')

    go = go.lower().split()

    # if they type 'go' first
    if go[0] == 'go' or 'move':
        # check that they are allowed wherever they want to go
        if go[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][go[1]]
        # there is no door (link) to the new room
        elif go[1].lower() not in ['north','south','east', 'west']:
            print('Thats not a direction I recognise')
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if go[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if 'item' in rooms[currentRoom] and go[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [go[1]]
            # display a helpful message
            print(go[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + go[1] + '!')


    # player wins if they get to the garden with a key and a shield
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
