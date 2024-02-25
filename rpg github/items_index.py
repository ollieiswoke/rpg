#-----------------------------------------------------------------------------#
import items_class

green_potion = items_class.Potion("green_potion", "its green.", 11)
fizz_drink = items_class.Potion("fizz_drink", "Fills you with energy.", 17)
pocky =  items_class.Potion("pocky", "A sweet yummy snack.", 20)
#pocky
#jelly

pink_pill = items_class.Potion("pink_pill", "is it really a pill? maybe its a tic tac..", 10)
skull_drink = items_class.Potion("skull_drink", "Has a neutral yet milky flavour", 14)


#-----------------------------------------------------------------------------#
fireball = items_class.Weapon("fireball", "A very powerful spell.", 10)
talk = items_class.Weapon("talk", """communicates your FEELINGS.
lets people know what you're REALLY thinking
(not very effective)""", 5)
bat =  items_class.Weapon("bat", "An oak baseball bat.", 4)
sword = items_class.Weapon("sword", "sharp. It has a sort of dull shine", 4)
gauntlet = items_class.Weapon("gauntlet", "too big for your hand", 6)
amulet = items_class.Weapon("amulet", "Yun's special amulet. Grants her extra agility", 7)
knuckles = items_class.Weapon("knuckles", "Brass Knuckles", 18)
#-----------------------------------------------------------------------------#
house_map = """
 ----------        ----------       ------------        ----------
|          |      |          |     |            |      |          |
|  pool    | ~~~~ |  garden  | ~~~ |  stairway  | ~~~~ |  beach   |
 ----------        ----------       ------------        ----------
     |                 |
 ----------        ----------
|          |      |          |
| bedroom  | ~~~~ | kitchen  |
 ----------        ----------
                       |
                   ----------
                  |          |
                  | balcony  |
                   ----------
"""
beach_map = """
 ----------
|          |
|  cafe    |
 ----------
     |
 ----------        -----------         ----------
|          |      |           |       |          | ~~~~~~+
| footpath | ~~~~ | boardwalk | ~~~~~ | rockpools| ~~~~~~+
 ----------        -----------         ----------        |
                       |                                 |
 ~   ~    ~        ----------       ``` ``        ++=============++
                  |          |                    || FINAL AREA: ||
__________   +====|  beach   |     ~ocean~        || LOOKOUT     ||
stairway..|==|     ----------               ~ ~   ++=============++
----------

"""
help_msg = """
                W O A H      T H E R E
welcome to NULL! the aim of this game is to fight all the enemies
(in a friendly manner) and get to the LOOKOUT for your final showdown.
...remember... each character has their own strengths and weaknesses.

If you're having trouble..
    -try making your way to the beach (if you are stuck)
    -try restarting the game with a different character
    -press Ctrl + C to quit the game.
"""
