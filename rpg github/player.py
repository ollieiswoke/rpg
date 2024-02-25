import room_index
import items_index
class Player:
    def __init__(self, coord, name, health, max_health, potions, weapons, equipped_weapon, music):
        self.coord = coord
        self.name = name
        self.health = health
        self.room = room_index.ri[coord]
        self.potions = potions
        self.weapons = weapons
        self.equipped_weapon = equipped_weapon #eqipped item MUST BE AN ITEM. NOT A LIST
        self.max_health = max_health
        self.map = items_index.house_map
        self.music = music
    def game_over(self):
        print("""

        Y O U   D I E D

                                Y O U   D I E D
                                Y O U   D I E D
                                Y O U   D I E D
        """)
        while True:
            input(">>> pls rerun main.py to restart...")
    def you_win(self):
            print("""

            Y O U   W I N !    :)

                                    Y O U   W I N !
                                    Y O U   W I N !
                                    Y O U   W I N !

                    thank you for playing!
            """)
            while True:
                input(">>> rerun main.py to restart...")

    def player_fight_menu(self, enemy):
        #gives player options to inspect, check inventory, and fight. eventually player has to choose fight


        while True:
            print("""
            |  fighting {}!
             -------------------------------------------
            | ~o p t i o n s~                           |
            |  "fight" enemy        (or 'f')            |
            |  "look" at enemy      ('l'))              |
            |  look at inventory    ("invent" or 'i')   |
             -------------------------------------------
          """.format(enemy.name))
            command = input("command: ")
            if command == 'look' or command == 'l':
                print("""
              +-- {} --+
                |
                | hp: {}
                | atk: {}
| {}
                |""".format(enemy.name, enemy.health, enemy.atk, enemy.info))
                input('>>> (press enter)')
            elif command == 'invent' or command == 'i':
                self.select_items_menu()
            elif command == "fight" or command == "f":
                break
            else:
                print("That's not a command. Please try again")
                input(">>> (press enter)")
    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            #players turn: calls the fight menu.
            self.player_fight_menu(enemy)
            print("fighting {}...".format(enemy.name)) #fighting... display damage and minus health from enemy
            print("{}'s HP: {} --> {} ".format(enemy.name, enemy.health, enemy.health - self.equipped_weapon.atk))
            enemy.health = enemy.health - self.equipped_weapon.atk
            input(">>> (press enter)")
            if enemy.health <= 0: #if that attack just killed enemy, break the loop (so the dead enemy can't attack back)
                break
            print("^^ {}  a t t a c k s ^^".format(" ".join(list(enemy.name))))
            print("++------------------------++")
            print("{}'s HP: {} --> {}".format(self.name, self.health, self.health - enemy.atk))
            self.health = self.health - enemy.atk
            print("++------------------------++")
            input(">>> (press enter)")
        #the while loop has ended, so therefore one character has died.
        if enemy.health <= 0: #if bad guy health < 0
            print("""

            E N E M Y   D E F E A T E D                 *  *  *  *
                                                       *          *
                                                        *  *  *  *
            """)
            if enemy.name == "FINAL BOSS: THE PROFESSOR": #if the player just killed the final boss:
                self.you_win()
            if enemy.potion_drops or enemy.weapon_drops: #WOKE. #if at least one of these lists is not empty
                print(enemy.name + ' dropped...')
                for i in enemy.potion_drops:    #print out contents
                    print(i.name)               #add contents to inventory
                    self.potions.append(i)
                for i in enemy.weapon_drops:
                    print(i.name)
                    self.weapons.append(i)


            input(">>> (press enter)")
            self.room.has_enemy = False    #change the room values to not have an enemy
        # give player drops etc
        if self.health <= 0:
            self.game_over() #call the "if dead" function

        #       tell info, deal damage to player
    def move(self, ri, direction): #requires player, and ri dictionary
        #move to corresponding direction by editing co ord, and changed the room object to match with the coord (using the dictionary ri)
        if direction == "right":
            self.coord = (self.coord[0] + 1, self.coord[1])
        if direction == "left":
            self.coord = (self.coord[0] - 1, self.coord[1])
        if direction == "up":
            self.coord = (self.coord[0], self.coord[1] + 1)
        if direction == "down":
            self.coord = (self.coord[0], self.coord[1] - 1)
        self.room = ri[self.coord]
        print("====================")
        print("       moved!")
        print("====================")
        if self.room.has_enemy == True: #if there is an enemy in the new room... then fight it
            print("An enemy appeared!")
            input(">>> (press enter)")
            self.fight(self.room.enemy)  #calls the fight function on the enemy in room
    def use_potion(self, potion):
        print("        consuming {}...".format(potion.name))
        print("""        ====================
        {}'s HP: {} --> {}
        ====================""".format(self.name, str(self.health), str(min(self.health + potion.hp_power, self.max_health))))
        self.health = min(self.health + potion.hp_power, self.max_health) #if the potion heals above the max health, reduce it back to the maximum
        self.potions.remove(potion) #deletes the first found item that matches "potion".
    def equip_weapon(self, weapon):
        print("        equiping {}...".format(weapon.name))
        print("""        ====================
        new weapon: {}, atk = {}
        ====================""".format(weapon.name, str(weapon.atk)))
        self.weapons.remove(weapon) #remove the selected weapon from inventory
        self.weapons.append(self.equipped_weapon) #add eqipped item to the inventory
        self.equipped_weapon = weapon  #change the "eqipped_item" variable to the new weapon
    def show_items_menu(self):
        print("""
    ++++ I T E M   S E L E C T ++++

       ++weapons++""")

        self.weapon_names = []
        for w in self.weapons:
            self.weapon_names.append(w.name)
            print("     "+w.name)
        if self.weapons == []:
            print("     (no weapons)")
        print("")
        if self.equipped_weapon == []:
            print("     no weapon equipped")
        else:
            print("     "+self.equipped_weapon.name+" is currently equipped.")
        print("""
        """)

        print("""

       ++potions++""")

        self.potion_names = []
        for p in self.potions:
            self.potion_names.append(p.name)
            print("     "+p.name)
        if self.potions == []:
            print("     (no potions)")
        print("")
        print("")
        print("""

            | type 'check [item_name]' to find out about item
            | type 'use [item_name]' to equip or consume item
            |       (include underscores if they're in the title)
            | type 'exit' to exit
        """)

    def select_items_menu(self):
        while True: #loop asking for player command
            self.show_items_menu()
            item_choice = input("command: ")
            item_choice = item_choice.split(" ") #split into "use" and "item"
            if len(item_choice) > 2:    #validating to see if a its a real command
                print("Not a possible item command. Too many words.")
                continue
            elif item_choice[0] == 'use' and item_choice[1] == self.equipped_weapon.name:
                print('!!! That item is already equipped  !!!')
                #^^ specific error message for if player tries to equip the already equipped item
                continue
            elif item_choice[0] == 'exit':    #if exit is called, end the while loop
                break
            elif len(item_choice) == 1:       #if its still 1 word even though its not 'exit', than raise error
                print("Not a possible item command. :o")
                continue
            elif (item_choice[1] in self.potion_names) or (item_choice[1] in self.weapon_names): #if it is an available weapon
                print('')
            elif item_choice[0] == 'check' and item_choice[1] == self.equipped_weapon.name:
                print('')
                #^^SPECIAL CASE. if     they are trying to check the equpped weapon
                 #let it pass to the next stage (where action will take place)
            else:
                print("Not a possible item command. :(")
                continue    #restart the loop (ask the player again)


            #we've assumed the string is valid, so now find the correlating item
            item_code_as_a_string = 'items_index.' + item_choice[1] #mutilate string till it becomes "items_index.[item]"
            item_from_choice = eval(item_code_as_a_string) #than use that to find correlating item

            if item_choice[0] == 'check': #if player is checking an item
                if item_choice[1] in self.potion_names: #if it is an available potion
                    item_from_choice.display()  #display item
                if item_choice[1] in self.weapon_names: #if it is an available weapon
                    item_from_choice.display()  #display item
                if item_choice[1] == self.equipped_weapon.name:
                    item_from_choice.display()
            if item_choice[0] == 'use': #if player is using an item
                if item_choice[1] in self.potion_names: #if it is a potion (rather than a weapon)
                    self.use_potion(item_from_choice)
                if item_choice[1] in self.weapon_names: #if it is an available weapon
                    self.equip_weapon(item_from_choice)
