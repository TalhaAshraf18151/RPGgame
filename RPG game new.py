#!/bin/python3
import sys
import time

directions = ['up', 'down', 'right', 'left']
commands = ['up', 'down', 'right', 'left', 'interact']

def opening_screen():
    # print a main menu and the commands
    print('''
---------------------------   
Enviro schools RPG game 
By Talha Ashraf
Type 'interact' to begin'''
          )


def help_screen():
    print('''
Get to the Quiz_room and solve the challenge

Commands:''' + commands.__str__()

          )


def Status():
    # print the player's current status
    print('\n----------------------------')
    print('You are in ' + currentRoom)
    # print the current interactable
    if 'intractable' in rooms[currentRoom]:
        print('You see ' + rooms[currentRoom]['intractable'])


opening_messege = '''Welcome to the enviroschools RPG game. This game aims to educate you about plastic pollution 
in New Zealand. To win this game you have to find the Quiz_room and finish the challenge in it. 
To move type ''' + directions.__str__() + '''. Every room you are in will tell you it\'s name and the item in it.
To interact with the item type "interact". To get help at any time type "help". The next room is north of this one.
GLHF ^__^'''


def intractSpawn_room():
    for letter in opening_messege:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


info_1 = 'You must take information from the scroll of truth to the next room and answer the quiz'

scroll_of_truth='''
-Each New Zealander consumes approximately 31 kg of plastic packaging every single year
-Each New Zealander recycles approximately 5.58kgs of plastic packaging every single year
-Recycling a single plastic bottle can conserve enough energy to power a 60W bulb for 3 hours
'''

def intractScroll_room():
    print(info_1)
    for letter in scroll_of_truth:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


def intractTest_room():
    print('this will be the intraction in room 2')


def intractQuiz_room():
    print('this will be the intraction in room 3')

# a dictionary linking a room to other room positions
rooms = dict(Spawn_room={'up': 'Scroll_room',
                         'intractable': 'intro sheet',
                         'function': intractSpawn_room

                         }, Scroll_room={'down': 'Spawn_room',
                                   'right': 'Test_room',
                                   'intractable': 'Scroll of truth',
                                   'function': intractScroll_room

                                   }, Test_room={'left': 'Scroll_room',
                                             'down': 'Quiz_room',
                                             'intractable': 'Tablet',
                                             'function': intractTest_room

                                             }, Quiz_room={'left': 'Spawn_room',
                                                       'up': 'Test_room',
                                                       'intractable': '!Quiz_room',
                                                       'function': intractQuiz_room})





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

    elif input_user == 'help':
        help_screen()


    elif input_user not in directions or 'interact':
        print('invalid command')
        help_screen()


    # if they type 'interact' first

    #if input_user == rooms[currentRoom]['intractable']: