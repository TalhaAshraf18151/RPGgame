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
''' + directions.__str__() +
          '\n interact'
          )


def help_screen():
    print('''
    Get to the Garden with a key and a potion
Avoid the monsters!

Commands:''' + directions.__str__()+
          '\n interact'

          )


def Status():
    # print the player's current status
    print("\n" + currentRoom)
    # print the current interactable
    if 'intractable' in rooms[currentRoom]:
        print(rooms[currentRoom]['intractable'])

def intractSpawn_room():
    print('this will be the intraction in spawn room')


# a dictionary linking a room to other room positions
rooms = dict(Spawn_room={'up': 'room1',
                         'right': 'room4',
                         'intractable': 'intro sheet',
                         'function': intractSpawn_room

                         }, room1={'down': 'Spawn_room',
                                   'right': 'room2',
                                   'left': 'room3',
                                   'intractable': '!room1'

                                   }, room2={'left': 'room1',
                                             'down': 'room4',
                                             'intractable': '!room2'

                                             }, room3={'right': 'room1',
                                                       'intractable': '!room3'}, room4={'up': 'room2',
                                                                                        'left': 'Spawn_room',
                                                                                        'intractable': '!room4'})


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

win_status = 'loss'

# start the player in the Hall
currentRoom = 'Spawn_room'

opening_screen()

# loop forever
while win_status == 'loss':

    Status()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    input_user = ''
    while input_user == '':
        input_user = input('-')

    input_user = input_user.lower()

    # if they type 'go' first
    if input_user in directions:
        # check that they are allowed wherever they want to go
        if input_user in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][input_user]
        elif input_user not in directions:
            print('that\'s not a direction I recognise try ' + directions.__str__())
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    elif input_user == 'interact':
        callable(rooms[currentRoom]['function']())



    elif input_user not in directions or 'interact':
        print('invalid command')
        help_screen()


    # if they type 'interact' first

    #if input_user == rooms[currentRoom]['intractable']: