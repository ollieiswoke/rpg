import room_index
import player
import select_player
import items_class
import items_index
import enemy
import os
import sys
import random

character = "about to be player" #needs a variable for the next function
character = select_player.choose_character(character) #selects character. Puts player object in the character variable

from pygame import mixer
#locates files using relative referencing:
APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
song = random.choice(character.music)
full_path = os.path.join(APP_FOLDER, song)

mixer.init() #loads pygame mixer
mixer.music.load(full_path) #eg 'C:\Users\Ollie\Desktop\rpg\m- leo- prune'
mixer.music.play(loops=-1, start=0.0) #loops it

while True:
    if character.room.name == "beach": #if the character has reached a certain room..
        if character.map != items_index.beach_map:
            print('map has been changed!')
            character.map = items_index.beach_map
    if character.room.name == "stairway" and character.room.has_enemy == False: #if the character has reached a certain room.. (for the second time)
        if character.map != items_index.house_map:
            print('map has been changed!')
            character.map = items_index.house_map

    print("-- you are in {}, {} --".format(character.room.name, str(character.room.coord)))
    print("doors: {}".format(character.room.doors))
    print(character.map)
    print("""
    -) "move [direction]"         direction must be in doors. eg "move right"
    -) "invent"                   check inventory, equip items, etc
    -) "self"                     displays your health and atk
    -) "help"                     ask for help
    """)
    command = input("command: ")



    if command.split(' ')[0] == "move":
        if len(command.split(' ')) == 2: #if the command is 2 words
            if command.split(' ')[1] in character.room.doors: #if the second word is an available direction
                character.move(room_index.ri, command.split(' ')[1])
            else: #if the first word was 'move' but the second was not in 'doors'
                print("can't go that way :(         not in 'doors'")
                print("====================")
                print("====================")
                print("====================")
        else: #if the first word was 'move' BUT the length of the command != 2
            print("invalid command. type 'help' if you are stuck")
            input('>>> (press enter)')

    elif command == "invent":
        character.select_items_menu()

    elif command == 'self':
        print('     {}-     {}/{}hp, {} atk at the moment'.format(character.name, character.health, character.max_health, str(character.equipped_weapon.atk)))
        input('>>> (press enter)')

    elif command == 'help':
        print(items_index.help_msg)
        input('>>> (press enter)')

    else:
        print("invalid command. type 'help' if you are stuck")
        input('>>> (press enter)')
