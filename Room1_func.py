# Develop Room1 function here before plugging into main game
##

# Looking Glass

opening = '''
Whooosh!! 
you feel a chill in the air as you peer into the looking glass you  see an older version of yourself peering back.
You you stumble back scared.'''


def explore_func():
    print(
'''
To your left you see an infant in his cradle.\n
To your right is the sea.\n
behind you is a tall mountain.\n
What would you like to go do ?
''')
    answer2 = input('>')
    if 'baby' or 'infant' in answer2:
        print('''
        You move towards him and see he is drinking milk from his bottle. Looking closely at his milk you see
        microplastics in the milk. A voice from somewhere says
              you see''')

    if 'sea' in answer2:
        print('Sea works')
    elif 'water' in answer2:
        print('Sea works')


def interact_room1():
    print(opening)
    print('''Perhaps you want to look again or do you want to look around''')
    answer1 = input('>').lower().split()

    if "again" in answer1:
        print("You see the same thing")
        explore_func()
    elif "around" in answer1:
        explore_func()
    else:
        print("Invalid input")
        interact_room1()


interact_room1()
