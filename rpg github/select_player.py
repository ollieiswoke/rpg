import player
import items_index
#coord, name, health, potions, weapons, equipped weapon
pk = player.Player((0,1), "PK", 35, 35, [items_index.green_potion], [], items_index.bat, ['m- pk- hero.mp3', 'm- pk- plastic.mp3', 'm- pk- rain.mp3'])
yun = player.Player((0,1), "Yun", 20, 20, [items_index.skull_drink], [items_index.sword, items_index.gauntlet], items_index.amulet, ['m- yun- okra.mp3','m- yun- sweatpants.mp3','m- yun- daydream.mp3',])
leo = player.Player((0,1), "Leo", 30, 30, [], [items_index.talk], items_index.bat, ['m- leo- candles.mp3','m- leo- prune.mp3','m- leo- belly.mp3',])
snow = player.Player((0,1), "Snow", 40, 40, [items_index.green_potion, items_index.fizz_drink, items_index.pocky], [], items_index.sword,['m- snow- newark.mp3','m- snow- bonobo.mp3','m- snow- fish.mp3',])
molly = player.Player((5,2), "Molly", 30, 30, [], [], items_index.knuckles,['m- molly- sober.mp3',])

num2player = {'1': pk,
              '2': yun,
              '3': leo,
              '4': snow,
              '5': molly}


def choose_character(hyp_character):
    print("""
.______  .____     .___    .___    
:      \ |    |___ |   |   |   |   
|       ||    |   ||   |   |   |   
|   |   ||    :   ||   |/\ |   |/\ 
|___|   ||        ||   /  \|   /  \
    |___||. _____/ |______/|______/
 """)
    print("++CHOOSE YOUR CHARACTER++")
    while True:
        print("""
        1) {}       The main character.
                            a jack of all trades. medium health and strength.
                            listens to piano pop
        2) {}       Brings the party wherever she goes.
                            strong, but less health.
                            listens to rap
        3) {}       A lover, not a fighter.
                            can communicate his feelings.
                            listens to alt pop
        4) {}       Obsessive & overprepared.
                            starts w/ lots of potions.
                            listens to funky electronic music
        5) {}       A ghost
                            very powerful.
                            choose her if the game is too hard.
                            listens to 'Sober' by Childish Gambino.
        """.format(pk.name.upper(), yun.name.upper(), leo.name.upper(), snow.name.upper(), molly.name.upper()))
        player_choice = input("enter a number.. ")
        if player_choice in num2player:
            hyp_character = num2player[player_choice] #hyp_character is hypothetical character. they are determined by the dictionary of numbers to player objects
            print("""

            YOU HAVE SELECTED {}


            """.format(hyp_character.name.upper()))
            input(">>> (press enter)")
            return hyp_character
        print("not an available character :( please enter a corresponding number")
