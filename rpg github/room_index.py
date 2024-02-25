import enemy

class Room:
    def __init__(self, x, y, name, doors):
        self.x = x
        self.y = y
        self.coord = (x, y)
        self.name = name
        self.doors = doors
        self.has_enemy = False

        #the items list would reference some Item class objects...
        items = []

class Fightroom(Room):
    def __init__(self, x, y, name, doors, enemy):
        Room.__init__(self, x, y, name, doors)
        self.has_enemy = True
        self.enemy = enemy

bedroom = Room(0,0, "bedroom", ["up", "right"])
kitchen = Fightroom(1,0, "kitchen", ["up", "left", "down"], enemy.skull_joe)
garden = Room(1,1, "garden", ["left", "down", "right"])
pool = Room(0,1, "pool", ["right", "down"])
stairway = Fightroom(2,1, "stairway", ["left", "right"], enemy.blue_boyo)
balcony = Fightroom(1, -1, "balcony", ["up"], enemy.one_eye)
beach = Room(3,1, "beach", ["up", "left"])
boardwalk = Room(3,2, "boardwalk", ["down", "left", "right"])
footpath = Room(2,2, "footpath", ["right", "up"])
cafe = Fightroom(2,3, "cafe", ["down"], enemy.the_twins)  #secret boss with cool item drop
rockpools = Fightroom(4,2, "rockpools", ["right", "left"], enemy.goblin_squad) #pre boss
lookout = Fightroom(5,2, "lookout", ["left"], enemy.the_professor) #final boss


ri = {bedroom.coord: bedroom, #room coord match to room object
              kitchen.coord: kitchen, #ri stands for Room Index
              garden.coord: garden,
              pool.coord: pool,
              stairway.coord: stairway,
              balcony.coord: balcony,
              beach.coord: beach,
              boardwalk.coord: boardwalk,
              footpath.coord: footpath,
              cafe.coord: cafe,
              rockpools.coord: rockpools,
              lookout.coord: lookout
              }
