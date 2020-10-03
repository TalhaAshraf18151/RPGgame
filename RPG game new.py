#!/bin/python3


directions = ['up', 'down', 'right', 'left']

def opening_screen():
    # print a main menu and the commands
    print('''
RPG Game
========

Get to the Garden with a key and a potion
Avoid the monsters!

Commands:
 go [direction] ''' 'valid directions = ' + directions.__str__() +
  '\n interact'
)


def help_screen():
    print('''
    Get to the Garden with a key and a potion
Avoid the monsters!

Commands:
 go [direction] ''' 'valid directions' + directions.__str__() +
  '\n interact'

          )

def Status():
    # print the player's current status
    print("\n" + currentRoom)
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


def intractSpawn_room():
    print('this will be the intraction in spawn room')



def intractroom1():
    print('this will be the intraction in room1')

def intractroom2():
    print('this will be the intraction in room 2')


def intractroom3():
    print('this will be the intraction in room 3')

def intractroom4():
    print('this will be the intraction in room 4')

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
        input_user = input('-')

    input_user = input_user.lower().split()

    currentRoom = currentRoom

    # if they type 'interact'
    if input_user[0] == 'interact':
        if currentRoom == 'Spawn_room':
            intractSpawn_room()

    if input_user[0] == 'interact' and currentRoom == 'room1':
        intractroom1()

    if input_user[0] == 'interact' and currentRoom == 'room2':
        intractroom2()

    if input_user[0] == 'interact' and currentRoom == 'room3':
        intractroom3()

    if input_user[0] == 'interact' and currentRoom == 'room4':
        intractroom4()



    # if they type 'go' first
    if input_user[0] == 'go' or 'move':
        # check that they are allowed wherever they want to go
        if input_user[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][input_user[1]]
        elif input_user[1] not in directions:
            print('thats not a direction I recognise try ' + directions.__str__())
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')




   # else:
    #    help_screen()

    # player wins if they get to the garden with a key and a shield
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break
