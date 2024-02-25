import items_index

class Enemy:
    def __init__(self, name, health, info, atk, potion_drops, weapon_drops):
        self.name = name
        self.health = health
        self.info = info
        self.atk = atk
        self.potion_drops = potion_drops
        self.weapon_drops = weapon_drops

skull_joe = Enemy("Skull Joe", 25, """A weird looking fella. He's very short and he's wearing a skull mask""", 2, [items_index.skull_drink, items_index.skull_drink], [])
#drops 'skull drink'

blue_boyo = Enemy("Blue Boyo!", 8, """He's wearing an oversized shirt that is light blue.
| his face is painted blue, or is it just like that ...? """, 3, [items_index.pink_pill], []) # drops a potion)

goblin_squad = Enemy("Goblin Squad", 10, """
| oh no! the whole crew's here! They all think they are much cooler than you... """, 6, [items_index.green_potion], [])
#drops skull drink x2

one_eye = Enemy("One Eye", 17, """One eye is pink and the other is brown.
| They have their signature gauntlet with them.""", 6, [], [items_index.gauntlet])

the_twins = Enemy("""SECRET BOSS: THE TWINS""", 21, """two fashionable twins. They're both
| wearing hoodies and casting magic toward you!""", 8, [items_index.fizz_drink, items_index.pocky], [items_index.fireball])


the_professor = Enemy("FINAL BOSS: THE PROFESSOR", 22, "...", 7, [], [])
