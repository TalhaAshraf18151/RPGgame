# !/bin/python3

## BY TALHA ASHRAF
import time
import sys

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
    print('You are in ' + current_room)
    # print the current interactable
    if 'intractable' in rooms[current_room]:
        print('You see ' + rooms[current_room]['intractable'] + "\n")


#function for recording user's name and greeting
name = ""
def namefunc():
    global name
    print('What is your name?')
    name += input("\n>")
    print('\nNice to meet you ' + name)



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
*reading scroll*
-Each New Zealander consumes approximately 31 kg of plastic packaging every single year
-Each New Zealander recycles approximately 5.58kgs of plastic packaging every single year
-Recycling a single plastic bottle can conserve enough energy to power a 60W bulb for 3 hours
-New Zealand waterways carry approximately 4,000,000 tonnes of plastic to sea
-Plastic waste leeches toxic chemicals into our waterways killing animals and putting humans at risk

Those are just some facts but I would like help you think deeper into the problem. We like to blame  people like you and
I for disposing of their plastic irresponsibly  but why does nobody talk about how manufacturers continue to use single 
use plastic packaging while being well aware of its impact. I urge you to not only dispose of plastic responsibly so
that it does not cause any more harm to the environment but also to raise your voice to spread awareness about plastic 
so other people can play their role as well.
'''


#Runs when user interacts with item in Scroll_room

def intractScroll_room():
    print(info_1)
    for letter in scroll_of_truth:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)



ending_messege = '''Thank you so much for playing my game. I hope that it inspires you to think about the way you throw 
away your plastic and the consequences of your actions'''



#score checker function
#will end game if score is highest (5)
#will deposit person back into Quiz_Room if not 5
def score_check():
    if correct_answers == 5:
        print("###################"
              " GOOD JOB YOU WON !! "
              "###################")
        time.sleep(5)
        for letter in ending_messege:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.03)
        exit()
    elif correct_answers == 4:
        print("Try again. You're so close you got 3 right")
    elif correct_answers < 4:
        print("Try again you got " + correct_answers.__str__() + ' correct')




correct_answers = 0


#Quiz function that runs in the last room
#an input asks a question with a prompt
#if and elif statements used to deterimne if answer is correct
def intractQuiz_room():
    #records time when function starts to determine total time taken at the end
    t0 = time.time()
    global correct_answers
    q1 = input("\nQ1) What should you do to a plastic food wrapper after you have eaten the food? \na) Eat the wrapper as well\nb) Dispose of it in a bin\nc) Throw it on the ground\n>")
    if q1.lower() == "b":
        print("Good job correct answer\n")
        correct_answers += 1 #counter for score
    elif len(q1) > 1:
        print("\ninvalid command")
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nb) Dispose of it in a bin.")
    print('current score is ' + correct_answers.__str__())
    print("\n")

    q2 = input("\nQ2) How much plastic does the average New Zealander recycle? \na) 7.3 kg\nb) 5.58 kg\nc) 6.9 kg\n>")
    if q2.lower() == "b":
        print("Good job correct answer\n")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nb)5.58 kg\n")
    print('current score is ' + correct_answers.__str__())
    print("\n")

    q3 = input("How long can it take plastic to break down? \na) 9000 years\nb) 100 years\nc) 1000 years\n>")
    if q3.lower() == "c":
        print("Good job correct answer\n")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nc) 1000 years\n")
    print('current score is ' + correct_answers.__str__())
    print("\n")

    q4 = input("How much plastic does the each New Zealander use in a year?\na) 72 Kg\nb) 14 Kg\nc) 31\n>")
    if q4.lower() =="c":
        print("Good job correct answer\n")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \nc) 31 Kg\n")
    print('current score is ' + correct_answers.__str__())
    print("\n")

    q5 = input("Recycling a single plastic bottle conserves enough energy to power a 60W bulb for how long?\na) 30 mins\nb) 60 mins\nc) 20 mins\n>")
    if q5.lower() == "a":
        print("Good job correct answer\n")
        correct_answers += 1
    else:
        print("Oops, seems like you are incorrect the correct answer is actually \na) 30 mins\n")
    t1 = time.time() - t0
    print("It only took you " + round(t1).__str__() + " seconds")
    score_check()


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
current_room = 'Spawn_room'

opening_screen()

# loop forever
while True:

    Status()
    
    # get the player's next 'move'
    input_user = ''
    while input_user == '':
        input_user = input('>')

    input_user = input_user.lower()

    #check if input is a direction
    if input_user in directions:
        # check that they are allowed wherever they want to go
        if input_user in rooms[current_room]:
            # set the current room to the new room
            current_room = rooms[current_room][input_user]
        elif input_user not in directions:
            print('that\'s not a direction I recognise try ' + directions.__str__())
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
    # calls function for room
    elif input_user in ['interact', 'read', 'pick']:
        callable(rooms[current_room]['function']())
    # if user asks for help
    elif input_user == 'help':
        help_screen()

    # deals with unusable values
    elif input_user not in directions or 'interact':
        print("---------------------------")
        print('\ninvalid command')
        help_screen()
