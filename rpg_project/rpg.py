#!/usr/bin/python3
import requests
import random
import html

garden_door_locked = True
game_over = False

def show_instructions():
  print('''
    RPG Game
    ========
    Commands:
    go [direction]
    get [item]
''')

# helper method to get room description
def get_room_desc():
    directions = ['north', 'south', 'east', 'west', 'downstairs', 'upstairs']
    desc = f'You are in the {current_room}.'

    # check if directions to connecting rooms exist in current room dict and add to description
    for direction in rooms[current_room].keys():
        if direction in directions:
            desc += f' {rooms[current_room][direction]} is {direction}.'

    return desc

def show_status():
  print('---------------------------')
  # get room description
  print(get_room_desc())
  print('Inventory : ' + str(inventory))
  if "item" in rooms[current_room]:
    print('You see a ' + rooms[current_room]['item'])
  print("---------------------------")
        
inventory = []

rooms = {
    'Hall' : {
            'south' : 'Kitchen',
            'east'  : 'Dining Room',
            'item'  : 'key',
            'secret': 'Library'
        },
    'Kitchen' : {
            'north' : 'Hall',
            'item'  : 'monster'
        },
    'Dining Room' : {
            'west' : 'Hall',
            'east' : 'Living Room',
            'item' : 'potion',
            'north' : 'Pantry',
        },
    'Garden' : {
            'north' : 'Library',
        },
    'Pantry' : {
            'south' : 'Dining Room',
            'item' : 'cookie',
    },
    # add Living Room
    'Living Room': {
            'west' : 'Dining Room',
            'south' : 'Library',
    },
    # add Library
    'Library': {
            'north' : 'Living Room',
            'south' : 'Garden'
    },
}

current_room = 'Hall'

show_instructions()

def enter_library_trivia():
    trivia_url = 'https://opentdb.com/api.php?amount=3&category=10&difficulty=easy&type=multiple'
    trivia_api = requests.get(trivia_url).json()
    attempts = 0
    correct = 0
    choices = []

    for result in trivia_api['results']:
        # add all possible answers to choices list
        choices.append(result['correct_answer'])
        choices += result['incorrect_answers']
        # randomize choices so that correct answer is not always first in the list
        random.shuffle(choices)

        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice}")
    
        answer = input(f"\n{html.unescape(result['question'])} Select 1, 2, 3, or 4\n>").lower()
        attempts += 1
        stats = f"{correct + 1} out of {attempts} correct"
        print('---------------------------')

        if (choices[int(answer) - 1] == result['correct_answer']):
            correct += 1
            print('Correct!', correct)
            print(stats)
        else:
            print('Incorrect!')
            print(stats)
        
        print('---------------------------')
        # reset choices
        choices = []
    
    if correct == 3:
        global garden_door_locked 
        garden_door_locked = False
        print('You did it! You may now enter the garden')
    else:
        print('You are not worthy! You cannot enter the Garden until you answer 3 questions correctly in a row!')

while not game_over:
  show_status()
  move = ''

  while move == '':
    move = input('>')         
    move = move.lower().split(" ", 1)

    if move[0] == 'go':
        dining_to_living = current_room == 'Dining Room' and move[1] == 'east'
        living_to_dining = current_room == 'Living Room' and move[1] == 'west'
        library_to_garden = current_room == 'Library' and move[1] == 'south'

        #check locked door scenarios
        if dining_to_living or living_to_dining:
            print('The door is locked! Try a different direction.')
        #check library to garden scenario
        elif library_to_garden and garden_door_locked:
            print('The butler blocks you from exiting the library. You shall not enter the Garden unless you can answer 3 library questions!\n')
            enter_library_trivia()
        elif move[1] in rooms[current_room]:
            current_room = rooms[current_room][move[1]]
        else:
            print('You can\'t go that way!')

    if move[0] == 'get' :
        if "item" in rooms[current_room] and move[1] in rooms[current_room]['item']:
            inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[current_room]['item']
        else:
            print('Can\'t get ' + move[1] + '!')

    # Check if player is in room with monster
    is_player_with_monster = 'item' in rooms[current_room] and 'monster' in rooms[current_room]['item']
    
    ## Win condition (player escapes through garden with key and potion)
    if current_room == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        game_over = True
        break

    # Unlock secret staircase which transports player from Kitchen to Living Room.
    if is_player_with_monster and 'cookie' in inventory:
        # remove cookie from inventory
        inventory.remove('cookie')
        # remove monster from kitchen
        del rooms[current_room]['item']
        # add secret access between living room and kitchen via stairs
        rooms[current_room]['downstairs'] = "Living Room"
        rooms['Living Room']['downstairs'] = "Kitchen"
        # notify player of secret unlocked
        print('A monster runs away with your cookie, knocking down the fridge. A secret underground staircase is revealed!')

    ## Lose condition (player enters kitchen without a cookie gets eaten by monster)
    elif is_player_with_monster:
        print('A monster has got you... GAME OVER!')
        game_over = True
        break