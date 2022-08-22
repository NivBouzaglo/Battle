import random
from classes.Inventory import Item


class bcolors:
    HEADER ='\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # END THE COLOR LINE
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:

    def __init__(self, hp, mp, atk, df, magic, item):
        self.maxhp = hp  # score
        self.hp = hp
        self.maxmp = mp  # magic_points
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.item = item
        self.actions = ["Attack", "Magic", "Item"]

    def generate_damage(self):
        return random.randrange(self.atkl ,self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0

        return self.hp

    def heal(self , mad):
        self.hp += mad
        if self.hp > self.maxhp:
            self.hp = self.maxhp

        return self.hp


## getters

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self , cost):
        self.mp -= cost

    def get_magic_name(self , index):
        return self.magic[index]["name"]

    def get_magic_cost(self, index):
        return self.magic[index]["cost"]

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE +"Actions"+ bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + "Magic:" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + "." + spell.name + ", cost:", str(spell.cost))
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKBLUE + "Item:" + bcolors.ENDC)
        for item in self.item:
            print("    " + str(i) + "." + item["item"].name + ":", item["item"].description + " (x"+str(item["quantity"])+")")
            i += 1





