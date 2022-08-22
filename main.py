from classes.game import Person, bcolors
from classes.Magic import Spell

# Black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 15, 200, "black")
blizzard = Spell("Blizzard", 12, 150, "black")
meteor = Spell("Meteor", 20, 225, "black")
quake = Spell("Quake", 10, 100, "black")

# White magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

magic = [fire, thunder, blizzard, meteor, quake, cure, cura]

player = Person(450, 65, 60, 34, magic)
enemy = Person(500, 65, 45, 25, magic)

run = True

# when we want to wrap text with color
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACK!" + bcolors.ENDC)

while run:
    print("==================")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("you attacked for", dmg, "point of damage. Enemy HP:", enemy.get_hp())

    elif index == 1:
        player.choose_magic()
        magic_number = int(input("choose Magic:")) - 1

        spell = player.magic[magic_number]
        magic_dmg = spell.generate_spell_damage()
        curr_mp = player.get_mp()

        if spell.cost > curr_mp:
            print(bcolors.FAIL + "\nnot enough MP\n" + bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)
        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for " + str(magic_dmg) + bcolors.ENDC)
        else:
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg) + bcolors.ENDC)

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)

    print("Enemy attacked for", enemy_dmg)
    print("-----------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp())+"/" + str(enemy.get_max_hp())+"\n" + bcolors.ENDC)
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp())+"/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp())+"/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
        run = False

    if player.get_hp() == 0:
        print(bcolors.FAIL + "You were defeated by your enemy!!" + bcolors.ENDC)
        run = False
