import pygame
import textwrap
import math

pygame.init()

class Background:
    def __init__(self, background, x=0, y=0):
        self.background = pygame.image.load(background)
        self.width = 1280
        self.height = 720
        self.x = x
        self.y = y

    def draw(self):
        window.blit(self.background, (self.x, self.y))

class Button:
    """
                                    Documentation

        init - inicjalizacja ustawień buttona
        draw - rysowanie buttona, animacja na najazd myszki

    """

    def __init__(self, x, y, width, height, images, changeable, able_press, typeofinfo, info=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.images = []
        for image in images:
            self.images.append(pygame.image.load(image))
        self.image = self.images[0]
        self.able_press = able_press
        self.changeable = changeable  # Czy możliwa animacja (hover)
        self.change = False  # Stan animacji, czy myszka najechała (hover state)
        self.typefoinfo = typeofinfo
        self.info = Text(0, 0, info, 10, self.typefoinfo)
        self.visability = True

    def draw(self):
        global window
        if self.changeable:
            if self.change == True:
                self.image = self.images[1]
            else:
                self.image = self.images[0]
        window.blit(self.image, (self.x, self.y))

    def onclick(self):
        pass


class Chat(Button):
    def __init__(self, x, y, width, height, images, changeable, able_press, typeofinfo, info):
        Button.__init__(self, x, y, width, height, images, changeable, able_press, typeofinfo, info)
        self.chat_queue = []

    def draw_message(self):
        for message in self.chat_queue:
            message.draw()

    def get_text(self, text_obj):
        if len(self.chat_queue) > 10:
            self.del_text()
        self.chat_queue.append(text_obj)

    def del_text(self):
        self.chat_queue.pop(0)


class Text:
    def __init__(self, x, y, text, size, type):
        self.x = x
        self.y = y
        self.size = size
        self.raw_text = text
        self.type = type
        self.style = 'Times New Roman'
        self.fontt = pygame.font.SysFont(self.style, self.size)
        if type == "fight":
            # value = """This function wraps the input paragraph such that
            # each line in the paragraph is at most width
            # characters long. The wrap method returns a list of
            # output lines. The returned list is empty if the
            # wrapped output has no content."""(text)
            # Wrap this text.
            wrapper = textwrap.TextWrapper(width=50)
            string = wrapper.fill(text=text)
            self.text = self.fontt.render(string, 1, (255,255,255))
        elif type == "statistics" or type == "name_lvl_proff":
            self.text = self.fontt.render(text, 1, (255, 0, 0))
        else:
            self.text = self.fontt.render(text, 1, (255,255,255))

    def draw(self):
        window.blit(self.text, (self.x, self.y))

class Profession:
    def __init__(self, profession):
        self.step = 0
        self.hp_per_lvl = 0
        self.mana_per_lvl = 0
        self.mana_by_intelligence = 0
        self.power_per_strength = 0
        self.dodge_per_agility = 0
        self.crit_per_agility = 0
        self.strength_per_lvl = 0
        self.intelligence_per_lvl = 0
        self.agility_per_lvl = 0
        if profession == "Punisher":
            self.step = 0
            self.hp_per_lvl = 0
            self.mana_per_lvl = 0
            self.mana_by_intelligence = 0.1
            self.power_per_strength = 0.1
            self.dodge_per_agility = 0.1
            self.crit_per_agility = 0.1
            self.strength_per_lvl = 0
            self.intelligence_per_lvl = 0
            self.agility_per_lvl = 0
        elif profession == "Hitter":
            self.step = 0
            self.hp_per_lvl = 0
            self.mana_per_lvl = 0
            self.mana_by_intelligence = 0.1
            self.power_per_strength = 0.1
            self.dodge_per_agility = 0.1
            self.crit_per_agility = 0.1
            self.strength_per_lvl = 0
            self.intelligence_per_lvl = 0
            self.agility_per_lvl = 0
        elif profession == "Warrior":
            self.step = 0
            self.hp_per_lvl = 100
            self.mana_per_lvl = 10
            self.mana_by_intelligence = 0.1
            self.power_per_strength = 0.1
            self.dodge_per_agility = 0.1
            self.crit_per_agility = 0.1
            self.strength_per_lvl = 5
            self.intelligence_per_lvl = 2
            self.agility_per_lvl = 3
        elif profession == "Mage":
            self.step = 1
            self.hp_per_lvl = 0
            self.mana_per_lvl = 0
            self.mana_by_intelligence = 0.1
            self.power_per_strength = 0.1
            self.dodge_per_agility = 0.1
            self.crit_per_agility = 0.1
            self.strength_per_lvl = 0
            self.intelligence_per_lvl = 0
            self.agility_per_lvl = 0
        elif profession == "Archer":
            self.step = 2
            self.hp_per_lvl = 0
            self.mana_per_lvl = 0
            self.mana_by_intelligence = 0.1
            self.power_per_strength = 0.1
            self.dodge_per_agility = 0.1
            self.crit_per_agility = 0.1
            self.strength_per_lvl = 0
            self.intelligence_per_lvl = 0
            self.agility_per_lvl = 0


class Item(Button):  # TODO
    def __init__(self, images, name, cost, rprof, itype, rlvl, addstrength=0, addintelligence=0, addagility=0,
                 crit_hit=0, dmg=0, addhp=0, addmp=0, dodge=0, armor=0, attack_speed=0, heal_per_attack=0,
                 heal_per_round=0, heal_per_use=0, x=0, y=0):
        Button.__init__(self, images=images, x=x, y=y, width=32, height=32, changeable=False, able_press=True,
                        typeofinfo="", info="")
        self.cost = cost
        self.name = name
        self.rprof = rprof
        self.itype = itype
        self.rlvl = rlvl
        self.addstrength = addstrength
        self.addintelligence = addintelligence
        self.addagility = addagility
        self.crit_hit = crit_hit
        self.dmg = dmg
        self.addhp = addhp
        self.armor = armor
        self.dodge = dodge
        self.addmp = addmp
        self.attack_speed = attack_speed
        self.heal_per_attack = heal_per_attack
        self.heal_per_round = heal_per_round
        self.heal_per_use = heal_per_use
        self.uses = 1

pointer = 'img/pointer.png'
window = pygame.display.set_mode((1280, 720))
pygame.mouse.set_visible(False)
run = True
cursor = pygame.image.load(pointer).convert_alpha()