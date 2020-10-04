#Develop spawn room function here before plugging into main game

import sys
import time

directions = ['up', 'down', 'right', 'left']
opening_messege = '''To finish this game you have to find room three and finish the challenge in it.
To move type''' + directions.__str__() + '''
Every room will have something you can interact with. To interact with the object type "interact"
To get help at any time type "help"
The next room is above this one
GLHF ^__^'''

def intractSpawn_room():
    for character in opening_messege:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

intractSpawn_room()