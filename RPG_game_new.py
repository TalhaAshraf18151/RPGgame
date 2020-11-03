# !/bin/python3

## BY TALHA ASHRAF
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

#This function to be called when player needs help
def help_screen():
    print('''
Get to the Quiz_room and solve the challenge

Commands:''' + commands.__str__()

          )

#Status shows the current room and items
def Status():
    # print the player's current status
    print('\n----------------------------')
    print('You are in ' + currentRoom)
    # print the current interactable
    if 'intractable' in rooms[currentRoom]:
        print('You see ' + rooms[currentRoom]['intractable'])


#function for recording user's name and greeting
name = 'some'


def namefunc():
    global name
    print('What is your name?')
    name = input(">")
    print('Nice to meet you ' + name)



#Runs when user interacts with item in spawn room
def intractSpawn_room():
    namefunc()
    for letter in opening_messege:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)



opening_messege = '''Welcome to the enviroschools RPG game. This game aims to educate you about plastic pollution 
in New Zealand. To win this game you have to find the Quiz_room and finish the challenge in it. 
To move type ''' + directions.__str__() + '''. Every room you are in will tell you it\'s name and the item in it.
To interact with the item type "interact". To get help at any time type "help". The next room is *NORTH* of this one.
GLHF ^__^'''

info_1 = 'You must take information from the scroll of truth to the next room and answer the quiz'

scroll_of_truth = '''
-Each New Zealander consumes approximately 31 kg of plastic packaging every single year
-Each New Zealander recycles approximately 5.58kgs of plastic packaging every single year
-Recycling a single plastic bottle can conserve enough energy to power a 60W bulb for 3 hours
'''

#Runs when user interacts with item in Scroll_room

def intractScroll_room():
    print(info_1)
    for letter in scroll_of_truth:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)




correct_answers = 0

def intractQuiz_room():
    t0 = time.time()
    global correct_answers
    q1 = input("\nQ1) What should you do to a plastic food wrapper after you have eaten the food? \na) Eat the wrapper as well\nb) Dispose of it in a bin\nc) Throw it on the ground\n>")
    if q1 == "a":
        print("Good job correct answer")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nb) Dispose of it in a bin.")

    q2 = input("\nQ2) How much plastic does the average New Zealander recycle? \na7.3 kg\nb)5.58 kg\nc)6.9 kg\n>")
    if q2 == "b":
        print("Good job correct answer")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nb)5.58 kg")

    q3 = input("How long can it take plastic to break down? \na)9000 years\nb)100 years\nc)1000 years\n>")
    if q3 == "c":
        print("Good job correct answer")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nc)1000 years")

    q4 = input("Recycling a single plastic bottle conserves enough energy to power a 60W bulb for how long?\na)60 mins\nb)30 mins\nc)20 mins\n>")
    if q4 == "b":
        print("Good job correct answer")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nb)30 mins")


# a dictionary linking a room to other room positions
rooms = dict(Spawn_room={'up': 'Scroll_room',
                         'intractable': 'intro sheet',
                         'function': intractSpawn_room

                         }, Scroll_room={'down': 'Spawn_room',
                                         'right': 'Quiz_room',
                                         'intractable': 'Scroll of truth',
                                         'function': intractScroll_room

                                         }, Quiz_room={'left': 'Scroll_room',
                                                       'intractable': 'Quiz',
                                                       'function': intractQuiz_room


                                                       })

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

    input_user = input_user.lower()

    #check if input is a direction
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
    # calls function for room
    elif input_user in ['interact', 'read', 'pick']:
        callable(rooms[currentRoom]['function']())
    # if user asks for help
    elif input_user == 'help':
        help_screen()

    # deals with unusable values
    elif input_user not in directions or 'interact':
        print("---------------------------")
        print('invalid command')
        help_screen()
