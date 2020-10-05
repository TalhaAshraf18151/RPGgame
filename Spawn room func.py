#Develop spawn room function here before plugging into main game

import sys
import time

directions = ['up', 'down', 'right', 'left']
opening_messege = '''Welcome to the enviroschools RPG game. This game aims to educate you about plastic pollution 
in New Zealand. To win this game you have to find room three and finish the challenge in it. 
To move type ''' + directions.__str__() + '''. Every room you are in will tell you it\'s name and the item in it.
To interact with the item type "interact". To get help at any time type "help". The next room is north of this one
GLHF ^__^'''


def intractSpawn_room():
    for letter in opening_messege:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


intractSpawn_room()