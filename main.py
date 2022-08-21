from classes.game import Person, bcolors


magic = [{"name": "fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 12, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(450, 65, 60, 34, magic)
enemy = Person(500, 65, 45 ,25,magic)

run = True

##when we want to wrap text with color
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACK!" +bcolors.ENDC)

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
        magic_dmg = player.generate_spell_damage(magic_number)
        spell = player.get_magic_name(magic_number)
        cost = player.get_magic_cost(magic_number)

        curr_mp = player.get_mp()

        if cost > curr_mp:
            print(bcolors.FAIL+ "\nnot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n"+ spell + " deals " + str(magic_dmg) + bcolors.ENDC)


    enemy_choice = 1
    enemy_dmg =enemy.generate_damage()
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
