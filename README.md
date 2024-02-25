# rpg
A text-based rpg made in python in 2018. 
There are multiple characters, a hidden boss and more!!1! 

RPG conventions (rooms, enemies, loot, etc) are coded from the ground up using object oriented programming. 

`pygame` is used for to play music and sound effects.

### Snippet: Map
```
-- you are in beach, (3, 1) --
doors: ['up', 'left']

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



    -) "move [direction]"         direction must be in doors. eg "move right"
    -) "invent"                   check inventory, equip items, etc
    -) "self"                     displays your health and atk
    -) "help"                     ask for help

command:
```

### Snippet: Combat
```
An enemy appeared!
>>> (press enter)

            |  fighting Blue Boyo!!
             -------------------------------------------
            | ~o p t i o n s~                           |
            |  "fight" enemy        (or 'f')            |
            |  "look" at enemy      ('l'))              |
            |  look at inventory    ("invent" or 'i')   |
             -------------------------------------------

command: f
fighting Blue Boyo!...
Blue Boyo!'s HP: 8 --> 4
>>> (press enter)
^^ B l u e   B o y o !  a t t a c k s ^^
++------------------------++
PK's HP: 35 --> 32
++------------------------++
>>> (press enter)
```
