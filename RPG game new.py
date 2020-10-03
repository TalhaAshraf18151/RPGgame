#!/bin/python3

def opening_screen():
    # print a main menu and the commands
    print('''
RPG Game
========

Get to the Garden with a key and a potion
Avoid the monsters!

Commands:
  go [direction] directions: north, south, east, west 
  interact 
''')


def help_screen():
    print('''
    Get to the Garden with a key and a potion
    Avoid the monsters!

Commands:
  go [direction] direction: north, south, east, west 
  interact
    '''

          )

def Status():
    # print the player's current status
    print(currentRoom)
    # print the current interactable


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other room positions
rooms = {

    'Spawn_room': {'up': 'room1',
                   'right': 'room4',
                    'intractable': 'intro sheet'
                   },

    'room1': {'down': 'Spawn_room',
              'right': 'room2',
              'left': 'room3'
              },

    'room2': {'left': 'room1',
              'down': 'room4'

              },

    'room3': {'right': 'room1'},

    'room4': {'up': 'room2',
              'left': 'Spawn_room'}

}


def intrtact_Spawn():
    Pass

# start the player in the Hall
currentRoom = 'Spawn_room'


opening_screen()

# loop forever
while True:

    Status()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    input_user = ''
    while input_user == '':
        input_user = input('>')

    input_user = input_user.lower().split()

    # if they type 'go' first
    if input_user[0] == 'go':
        # check that they are allowed wherever they want to go
        if input_user[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][input_user[1]]
        elif input_user[1] not in directions:
            print('thats not a direction I recognise try ' + directions.__str__())
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'interact'
    if input_user[0] == 'interact':




        # if the room contains an item, and the item is the one they want to get
      #  if 'item' in rooms[currentRoom] and go[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
       #     inventory += [go[1]]
            # display a helpful message
        #    print(go[1] + ' got!')
            # delete the item from the room
         #   del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        #else:
            # tell them they can't get it
         #   print('Can\'t get ' + go[1] + '!')

    # player wins if they get to the garden with a key and a shield
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
