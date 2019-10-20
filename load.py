import copy
import pygame
import random
import math
from threading import Thread
import time
from loginmenu import *
from bugreport import *
from loaded_elements import *

class move_Button:

    def __init__(self, x, y, width, height, changeable, able_press, typeofinfo, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = pygame.Rect(x,y,width,height)
        self.able_press = able_press
        self.raw_text = text
        self.changeable = changeable
        self.change = False
        self.typefoinfo = typeofinfo
        self.visability = True
        self.text = Text(x+6,y+6,text,30,"fight_button")

    def draw(self):
        pygame.draw.rect(window,(255,255,255),self.border,2)
        self.text.draw()

    def onclick(self):
        _add_events = get_add_events()
        _add_events[0].fight_engine(self.raw_text)

class Fight:
    def __init__(self):
        Button.__init__(self,414, 0, 530, 720, ['img/gui/backgrounds/fightbackground_desert1_new.png'], False,
                                 True, "whatever", "INFO_Fight")
        _buttons = get_buttons()
        _my_character = get_my_character()
        self.id = "fight"
        self.characters = [_my_character]
        self.enemies = []
        self.loots = []
        self.dead_array = []
        self.fight_end = False
        self.buttons = []
        self.move_buttons = []
        self.turn_character = self.characters[0]
        self.choosed_enemy_index = 1
        self.draw_enemies()
        for menu_butt in _buttons:
            if menu_butt in shops:
                _buttons.remove(menu_butt)
        self.buttons.append(fightbackground_desert1)
        self.buttons.append(move_in_battle_panel)
        _my_character.set_as_button(414 + 230, 580, 32, 49, [warrior_outfit[1]], False, True)
        for enemy in self.enemies:
            enemy.y = 480 - enemy.height
            enemy.x = 414 + 210
        for char in self.characters:
            char.calc_battle_stats()
        self.set_abilities_enemy()
        set_buttons(_buttons)
        set_my_character(_my_character)

    def check_deads(self):
        for character in self.characters:
            if character.battle_health_points <= 0:
                character.dead_state = True
        _my_character = self.characters[0]
        if _my_character.dead_state == True:
            self.fight_end = True
            _my_character.images = [
                grave_my_character]
            print("My character is dead")
            return None
            # TODO:send text to chat and block buttons to block attack after fight and lose
        for enemy in self.characters:
            if enemy.dead_state == True:
                enemy.images = [grave_enemy]
                loot = self.draw_loots(enemy.drops)
                if loot != 0:
                    self.loots += loot
                self.dead_array.append(enemy)
                enemy.type = "Looser"
                if len(self.dead_array) == len(self.enemies) - 1:
                    self.fight_end = True
                    _my_character.images = [warrior_outfit[0]]
                    self.buttons = self.show_drop_window()
        if self.fight_end == True:
            self.buttons.append(close_button)
            return None

    def change_turn(self):
        if self.characters.index(self.turn_character) == len(self.characters)-1:
            self.turn_character = self.characters[0]
        else:
            i = self.characters.index(self.turn_character)
            self.turn_character = self.characters[i + 1]

    def calculate_dodge(self):
        dod = random.randrange(1, 101)
        if dod >= 1 and dod <= self.characters[self.choosed_enemy_index].battle_dodge:
            return True
        else:
            return False

    def calculate_crit_hit(self):
        crit = random.randrange(1, 101)
        if crit >= 1 and crit <= self.turn_character.battle_critical_chance:
            return True
        else:
            return False

    def calculate_legendary_abilities(self):#TODO
        pass

    def draw_loots(self, loots):
        chance_for_loot = {"Normal": range(1, 51), "Rare": range(51, 62), "Legendary": range(62, 63)}
        lottery_nb = random.randrange(1, 1001, 1)
        win = ""
        loot_opt = []
        if lottery_nb > 0 and lottery_nb < 63:
            for type in chance_for_loot.keys():
                if lottery_nb in chance_for_loot[type]:
                    win = type
                    break
            for loot in loots:
                if loot.type == win:
                    loot_opt += loot
            i = random.randrange(0, len(loot_opt))
            return loot_opt[i]
        else:
            return 0

    def show_drop_window(self):
        arrbuttons = []
        arrbuttons.append(drop_panel)
        w = drop_panel.width
        len = len(self.loots)
        for i, loot in enumerate(self.loots):
            loot.x = drop_panel.x + (math.floor(w * i / len))
            loot.y = drop_panel.y + 15
            loot.id = i
            arrbuttons.append(loot)
            accept_button.x = loot.x - 10
            accept_button.y = loot.y + 50
            accept_button.id = i
            arrbuttons.append(accept_button)
            deny_button.x = loot.x + 10
            deny_button.y = loot.y + 50
            deny_button.id = i
            arrbuttons.append(deny_button)
        return arrbuttons

    def draw(self):
        arr = self.buttons + self.characters
        for button in arr:
            window.blit(button.image, (button.x, button.y))
        for move_button in self.move_buttons:
            move_button.draw()
            # print("Text: {}".format(move_button.raw_text))
        rect = pygame.Rect(self.characters[self.choosed_enemy_index].x - 2, self.characters[self.choosed_enemy_index].y - 2,
                           self.characters[self.choosed_enemy_index].width + 4,
                           self.characters[self.choosed_enemy_index].height + 4)
        pygame.draw.rect(window, (0, 255, 255), rect,2)
        for char in self.characters:
            char.draw_hp_mp_bar()

    def draw_enemies(self):
        index = random.randrange(0, len(enemies))
        fightenemy = enemies[index]
        self.enemies.append(fightenemy)
        self.characters.append(fightenemy)

    def fight_engine(self,name_of_action):
        self.calculate_legendary_abilities()
        if name_of_action not in ["OffAbilities","DefAbilities"]:
            if name_of_action == "Step":
                step_button.use_skill()
            else:
                dodge_bool = self.calculate_dodge()
                if not dodge_bool:
                    crit_bool = self.calculate_crit_hit()
                    if crit_bool:
                        if name_of_action == "Attack":
                            attack_button.use_skill(2)
                        else:
                            for ability in self.characters[self.turn_character].abilities:
                                if ability.name == name_of_action:
                                    ability.use_skill(2)
                                    break
                    else:
                        if name_of_action == "Attack":
                            attack_button.use_skill(1)
                        else:
                            for ability in self.characters[self.turn_character].abilities:
                                if ability.name == name_of_action:
                                    ability.use_skill(1)
                                    break
                    #TODO add text to chat
                else:
                    for ability in self.turn_character.abilities:
                        if ability.name == name_of_action:
                            cost = ability.ret_cost()
                            self.turn_character.battle_mana_points -= cost
                            #TODO add text to chat
                            print("Dodge")
                            break
                #TODO create mechanic of everey_round_events
                self.check_deads()
                self.change_turn()
                while self.characters[0] != self.turn_character:
                    self.choosed_enemy_index = 0
                    self.enemy_round_ai()
                print("{} attacked".format(self.turn_character.name))
        else:
            self.generate_move_button(name_of_action)

    def onclick(self):
        check_mouse_position(self.buttons)
        check_mouse_position(self.characters)
        check_mouse_position(self.move_buttons)
        print("Onclick fight")

    def add_move_in_panel_buttons(self,char):
        enemy_hp_text = ""
        enemy_mp_text = ""
        my_character_hp_text = ""
        my_character_mp_text = ""
        if char == "Enemy":
            hp,mp = self.characters[self.choosed_enemy_index].return_hp(),self.characters[self.choosed_enemy_index].return_mp()
            # enemy_hp_text = Text(810,30,"Enemy hp: "+str(hp),20,"type")
            # enemy_mp_text = Text(810,60,"Enemy mp: "+str(mp),20,"type")
            print("Enemy hp: {} mp: {}".format(hp,mp))
            hp,mp = self.characters[0].return_hp(),self.characters[0].return_mp()
            # my_character_hp_text = Text(810, 90, "My character hp: " + str(hp), 20, "type")
            # my_character_mp_text = Text(810, 120, "My character mp: " + str(mp), 20, "type")
            print("My character hp: {} mp: {}".format(hp, mp))
        else:
            hp, mp = 0,0
            # enemy_hp_text = Text(810, 30, "Enemy hp: " + str(hp), 20, "type")
            # enemy_mp_text = Text(810, 60, "Enemy mp: " + str(mp), 20, "type")
            hp, mp = self.characters[0].return_hp(), self.characters[0].return_mp()
            # my_character_hp_text = Text(810, 90, "My character hp: " + str(hp), 20, "type")
            # my_character_mp_text = Text(810, 120, "My character mp: " + str(mp), 20, "type")
            print("Enemy hp: {} mp: {}".format(hp,mp))
            print("My character hp: {} mp: {}".format(hp, mp))
        arr = []
        if char == "Enemy":
            # arr = [attack_button, off_abilities_button,enemy_hp_text,enemy_mp_text,my_character_hp_text,my_character_mp_text]
            arr = [attack_button, off_abilities_button]
        elif char == "My_character":
            # arr = [step_button,def_abilities_button,enemy_hp_text,enemy_mp_text,my_character_hp_text,my_character_mp_text]
            arr = [step_button,def_abilities_button]
        self.move_buttons = []
        for ab in arr:
            self.move_buttons.append(ab)

    def generate_move_button(self,type_of_abilities):
        if type_of_abilities == "OffAbilities":
            return self.turn_character.offabilities
        elif type_of_abilities == "DefAbilities":
            return self.turn_character.defabilities
        else:
            print("Something went wrong in fight.generate_move_button")

    def enemy_round_ai(self):
        #TODO build normal artificial intelligence
        self.fight_engine("Attack")

    def set_abilities_enemy(self):
        self.characters[1].abilities = [attack_button]

class Accept_Button(Button):
    def __init__(self, x, y, width, height, images, changeable, able_press, info):
        Button.__init__(self, x, y, width, height, images, changeable, able_press, info)
        self.id = 0

    def onclick(self, buttons, loots):
        filtered_loot = [loot for loot in loots if loot.id == self.id]
        My_character.eq.append(filtered_loot[0])
        filtered_buttons = [button for button in buttons if button.id == self.id]
        for buttonr in filtered_buttons:
            buttons.remove(buttonr)
        return buttons


class Deny_Button(Button):
    def __init__(self, x, y, width, height, images, changeable, able_press, info):
        Button.__init__(self, x, y, width, height, images, changeable, able_press, info)
        self.id = 0

    def onclick(self, buttons, loots):
        filtered_buttons = [button for button in buttons if button.id == self.id]
        for buttonr in filtered_buttons:
            buttons.remove(buttonr)
        return buttons

class Skill(move_Button):

    def __init__(self,x, y, width, height, changeable, able_press, typeofinfo, text,name,cost,damage,_type,lvl):
        move_Button.__init__(self, x, y, width, height, changeable, able_press, typeofinfo, text)
        self.name = name
        self.describe = ""
        self.cost = cost
        self.damage = damage
        self.given_damage = 0
        self.type = _type
        self.lvl = lvl

    def use_skill(self,multiplier):
        print("Use skill unique for any skill")

    def ret_describe(self):
        return self.describe

    def ret_every_round_action(self):
        print("Should return its own every round effect if has")

    def ret_dmg(self):
        return self.damage

    def learn(self):
        print("What to do when character has learned it")

    def ret_cost(self):
        return self.cost

class skill_Attack(Skill):

    def __init__(self,x, y, width, height, changeable, able_press, typeofinfo, text):
        Skill.__init__(self,x, y, width, height, changeable, able_press, typeofinfo, text,"Attack",0,0,"type",1)

    def learn(self):
        pass

    def ret_describe(self):
        return "Attack has given {} damage points".format(self.given_damage)

    def use_skill(self,multiplier):
        _add_events = get_add_events()
        fight = _add_events[0]
        attacker = fight.turn_character
        choosed_enemy_index = fight.choosed_enemy_index
        self.given_damage = attacker.battle_attack_damage * multiplier
        fight.characters[choosed_enemy_index].battle_health_points -= self.given_damage
        set_add_events(_add_events)

class skill_Fireball(Skill):

    def __init__(self,x, y, width, height, changeable, able_press, typeofinfo, text):
        Skill.__init__(self,x, y, width, height, changeable, able_press, typeofinfo, text,"Fireball",20,100,"OffAbility",1)

    def learn(self):
        pass

    def ret_describe(self):
        return "Fireball has given {} damage points and ignited enemy on 3 rounds".format(self.given_damage)

    def use_skill(self,multiplier):
        _add_events = get_add_events()
        fight = _add_events[0]
        attacker_index = fight.turn_character
        choosed_enemy_index = fight.choosed_enemy_index
        self.given_damage = self.damage*self.lvl * multiplier
        fight.characters[choosed_enemy_index].battle_health_points -= self.given_damage
        set_add_events(_add_events)

class skill_Waterfall(Skill):

    def __init__(self,x, y, width, height, changeable, able_press, typeofinfo, text):
        Skill.__init__(self,x, y, width, height, changeable, able_press, typeofinfo, text,"Waterfall",40,100,"OffAbility",1)
        self.add_attack_damage = 5

    def learn(self):
        pass

    def ret_describe(self):
        return "Waterfall has given {} damage points and increased attack damage about {}".format(self.given_damage,self.add_attack_damage*self.lvl)

    def use_skill(self,multiplier):
        _add_events = get_add_events()
        fight = _add_events[0]
        attacker_index = fight.turn_character
        choosed_enemy_index = fight.choosed_enemy_index
        self.given_damage = self.damage * self.lvl * multiplier
        fight.characters[choosed_enemy_index].battle_health_points -= self.given_damage
        fight.characters[attacker_index].battle_attack_damage += self.add_attack_damage*self.lvl * multiplier
        set_add_events(_add_events)

class skill_Heal(Skill):

    def __init__(self,x, y, width, height, changeable, able_press, typeofinfo, text):
        Skill.__init__(self,x, y, width, height, changeable, able_press, typeofinfo, text,"Heal",50,400,"DefAbility",1)

    def learn(self):
        pass

    def ret_describe(self):
        return "Heal has revived {} health points".format(self.given_damage)

    def use_skill(self,multiplier):
        _add_events = get_add_events()
        fight = _add_events[0]
        attacker_index = fight.turn_character
        choosed_enemy_index = fight.choosed_enemy_index
        self.given_damage = self.damage * self.lvl * multiplier
        fight.characters[attacker_index].battle_health_points += self.given_damage
        set_add_events(_add_events)

class skill_Step(Skill):

    def __init__(self,x, y, width, height, changeable, able_press, typeofinfo, text):
        Skill.__init__(self,x, y, width, height, changeable, able_press, typeofinfo, text,"Heal",50,400,"DefAbility",1)

    def learn(self):
        pass

    def ret_describe(self):
        return "Character has made a step forward"

    def use_skill(self):
        _add_events = get_add_events()
        fight = _add_events[0]
        attacker_index = fight.turn_character
        choosed_enemy_index = fight.choosed_enemy_index
        fight.characters[attacker_index].battle_step += 1
        set_add_events(_add_events)

class Characters(Profession):
    def __init__(self, name, profession, gender, lvl, armor, attack_damage, attack_speed, heal_per_attack,
                 heal_per_round,
                 strength, intelligence, agility, critical_chance, health_points, mana_points, type, id):
        self.name = name
        self.profession = profession
        Profession.__init__(self, self.profession)
        self.gender = gender
        self.lvl = lvl
        self.abilities = []
        self.offabilities = []
        self.defabilities = []
        """         Base Stats      """
        self.armor = armor
        self.attack_damage = attack_damage
        self.attack_speed = attack_speed
        self.heal_per_attack = heal_per_attack
        self.heal_per_round = heal_per_round
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        self.critical_chance = critical_chance
        self.health_points = health_points
        self.mana_points = mana_points
        self.dodge = 0
        self.dead_state = False
        self.type = type
        self.id = id

        """         Actual Stats (Base + Items)      """
        self.actual_armor = self.armor
        self.actual_attack_speed = self.attack_speed
        self.actual_heal_per_attack = self.heal_per_attack
        self.actual_heal_per_round = self.heal_per_round
        self.actual_strength = self.strength + math.floor(self.lvl*self.strength_per_lvl)
        self.actual_intelligence = self.intelligence + math.floor(self.lvl*self.intelligence_per_lvl)
        self.actual_agility = self.agility + math.floor(self.lvl*self.agility_per_lvl)
        self.actual_attack_damage = self.attack_damage + math.floor(self.strength * self.power_per_strength)
        self.actual_critical_chance = self.critical_chance + math.floor(self.actual_agility*self.crit_per_agility)
        self.actual_health_points = self.health_points + math.floor(self.lvl*self.hp_per_lvl)
        self.actual_mana_points = self.mana_points + math.floor(self.lvl*self.mana_per_lvl) + math.floor(self.intelligence*self.mana_by_intelligence)
        self.actual_dodge = self.dodge + math.floor(self.agility*self.dodge_per_agility)

        self.stats = [self.actual_strength, self.actual_intelligence, self.actual_agility, self.actual_health_points,
                      self.actual_mana_points, self.actual_attack_damage, self.actual_armor, self.actual_attack_speed,
                      self.actual_critical_chance, self.actual_dodge, self.actual_heal_per_attack,
                      self.actual_heal_per_round]

        self.battle_step = 0
        self.battle_armor = 0
        self.battle_attack_damage = 0
        self.battle_attack_speed = 0
        self.battle_heal_per_attack = 0
        self.battle_heal_per_round = 0
        self.battle_strength = 0
        self.battle_intelligence = 0
        self.battle_agility = 0
        self.battle_critical_chance = 0
        self.battle_health_points = 0
        self.battle_mana_points = 0
        self.battle_dodge = 0

    def calc_battle_stats(self):
        """         Battle Stats      """
        self.battle_step = self.step
        self.battle_armor = self.actual_armor
        self.battle_attack_damage = self.actual_attack_damage
        self.battle_attack_speed = self.actual_attack_speed
        self.battle_heal_per_attack = self.actual_heal_per_attack
        self.battle_heal_per_round = self.actual_heal_per_round
        self.battle_strength = self.actual_strength
        self.battle_intelligence = self.actual_intelligence
        self.battle_agility = self.actual_agility
        self.battle_critical_chance = self.actual_critical_chance
        self.battle_health_points = self.actual_health_points
        self.battle_mana_points = self.actual_mana_points
        self.battle_dodge = self.actual_dodge

    def onclick(self):
        print("Onclick " + str(self.name))
        _add_events = get_add_events()
        i = _add_events[0].characters.index(self)
        _add_events[0].choosed_enemy_index = i
        _add_events[0].add_move_in_panel_buttons(self.type)
        set_add_events(_add_events)


    def set_as_button(self, x, y, width, height, images, changeable, able_press, typeofinfo="", info=""):
        Button.__init__(self, x, y, width, height, images, changeable, able_press, typeofinfo, info)


    def return_hp(self):
        return self.battle_health_points

    def return_mp(self):
        return self.battle_mana_points

    def draw_hp_mp_bar(self):
        x = self.x + self.width/2 - 40
        y = self.y - 20
        w = 80
        h = 20
        hprect_x = x + 2 + 76
        hprect_y = y + 2
        hprect_w = 0
        hprect_h = 0
        p_hp = math.ceil(((self.battle_health_points/self.actual_health_points)*100)/10)
        hprect_w = -(8*(10-p_hp))

        mprect_x = x + 2 + 76
        mprect_y = y + 12
        mprect_w = 0
        mprect_h = 0
        p_mp = math.ceil(((self.battle_health_points / self.actual_health_points) * 100) / 10)
        mprect_w = -(8 *(10- p_mp))

        if hprect_w >= 0:
            hprect_h = 0
            hprect_w = 0
        else:
            hprect_h = 6
        if mprect_w >= 0:
            mprect_h = 0
            mprect_w = 0
        else:
            mprect_h = 6

        # print("HPW: {} HPH: {}".format(hprect_w,hprect_h))
        # print("MPW: {} MPH: {}".format(mprect_w, mprect_h))

        self.hpandmana_panel = Button(x, y, w, h, ['img/gui/panels/hpandmana_panel.png'], False, False, "whatever", "INFO")
        self.hpandmana_panel.draw()
        hprect = pygame.Rect(hprect_x,hprect_y,hprect_w,hprect_h)
        mprect = pygame.Rect(mprect_x, mprect_y, mprect_w, mprect_h)
        pygame.draw.rect(window,(0,0,0),hprect)
        pygame.draw.rect(window, (0, 0, 0), mprect)

class My_character(Characters):
    def __init__(self, name, profession, gender="Male", lvl=1, armor=0, attack_damage=5, attack_speed=10,
                 heal_per_attack=1, heal_per_round=2,
                 strength=100, intelligence=100, agility=100, critical_chance=10, health_points=350, mana_points=30,
                 type="My_character", id=0):
        Characters.__init__(self, name, profession, gender, lvl, armor, attack_damage, attack_speed, heal_per_attack,
                            heal_per_round,
                            strength, intelligence, agility, critical_chance, health_points, mana_points, type, id)
        self.bag = []
        self.bag_maxlen = 30
        self.eq = {"Hamlet": 0, "Ring": 0, "Necklace": 0, "Gloves": 0, "Weapon": 0, "Chest": 0, "Shield": 0,
                   "Boots": 0}
        self.items_armor = 0
        self.items_attack_damage = 0
        self.items_attack_speed = 0
        self.items_heal_per_attack = 0
        self.items_heal_per_round = 0
        self.items_strength = 0
        self.items_intelligence = 0
        self.items_agility = 0
        self.items_critical_chance = 0
        self.items_health_points = 0
        self.items_mana_points = 0
        self.items_dodge = 0

    def calculate_stats(self):
        for type_of_item in self.eq.keys():
            self.items_armor += self.eq[type_of_item].armor
            self.items_attack_damage += self.eq[type_of_item].dmg
            self.items_attack_speed += self.eq[type_of_item].attack_speed
            self.items_heal_per_attack += self.eq[type_of_item].heal_per_attack
            self.items_heal_per_round += self.eq[type_of_item].heal_per_round
            self.items_strength += self.eq[type_of_item].addstrength
            self.items_intelligence += self.eq[type_of_item].addintelligence
            self.items_agility += self.eq[type_of_item].addagility
            self.items_critical_chance += self.eq[type_of_item].crit_hit
            self.items_health_points += self.eq[type_of_item].addhp
            self.items_mana_points += self.eq[type_of_item].addmp
            self.items_dodge += self.eq[type_of_item].dodge
        self.actual_armor = self.armor + self.items_armor
        self.actual_attack_damage = self.attack_damage + self.items_attack_damage
        self.actual_attack_speed = self.attack_speed + self.items_attack_speed
        self.actual_heal_per_attack = self.heal_per_attack + self.items_heal_per_attack
        self.actual_heal_per_round = self.heal_per_round + self.items_heal_per_round
        self.actual_strength = self.strength + self.items_strength
        self.actual_intelligence = self.intelligence + self.items_intelligence
        self.actual_agility = self.agility + self.items_agility
        self.actual_critical_chance = self.critical_chance + self.items_critical_chance
        self.actual_health_points = self.health_points + self.items_health_points
        self.actual_mana_points = self.mana_points + self.items_mana_points
        self.actual_dodge = self.items_dodge + math.floor(self.actual_agility / (3 * self.lvl))

        self.stats = [self.actual_strength, self.actual_intelligence, self.actual_agility, self.actual_health_points,
                      self.actual_mana_points, self.actual_attack_damage, self.actual_armor, self.actual_attack_speed,
                      self.actual_critical_chance, self.actual_dodge, self.actual_heal_per_attack,
                      self.actual_heal_per_round]


class Enemy(Characters):
    def __init__(self, name, profession, gender, lvl, armor, attack_damage, attack_speed, heal_per_attack,
                 heal_per_round,
                 strength, intelligence, agility, critical_chance, health_points, mana_points, type, id, drops, x, y,
                 width, height, imagies, changeable=False, able_press=True, ):
        Characters.__init__(self, name, profession, gender, lvl, armor, attack_damage, attack_speed, heal_per_attack,
                            heal_per_round,
                            strength, intelligence, agility, critical_chance, health_points, mana_points, type, id)
        self.set_as_button(x, y, width, height, imagies, changeable, able_press)
        self.drops = drops

class Shop(move_Button):

    def __init__(self):
        self.shop_matrix = []
        self.cost_matrix = []
        move_Button.__init__()#TODO
        self.xy_matrix = []
        self.buttons = []

    def draw(self):
        _buttons = get_buttons()
        _buttons.append(self.buttons)
        set_buttons(_buttons)

    def buy(self):
        _my_character = get_my_character()
        buy_state = _my_character.add_new_item(self)
        if buy_state != True:
            print("Not enought money or space in the bag") #TODO

    def del_shop(self):
        pass #TODO

    def show_details(self):
        #del self from buttons
        #draw window,item sizex2,details,draw "BUY" button TODO
        pass



"""                                             ALL VARIABLES TO LOAD                                               """
abilities = []
my_character = My_character("Initialization", "Profession")

shops = [shopswords_button, shopstaffs_button, shopshields_button, shoprings_button, shoppotions_button,
         shopnecklets_button,
         shopmaces_button, shopknifes_button, shophelmets_button, shophammers_button, shopgloves_button,
         shopboots_button,
         shopaxes_button, shopboots_button, shopchests_button,antimatter_cavity_button,arena_button,daily_lucky_button,
         fusion_side_button,theunderworld_button]

""" Bosses """
gardon_boss_outfit = Enemy("Gordon Goblin", "Warrior", "Male", 1, 25, 25, 1, 0, 0, 25, 25, 25, 0, 500, 100, "Enemy", 0,
                           [axe_outfit], 0, 0, 65, 59, ['img/characters/bosses/gardon_boss_outfit.png'], False, True)
blodister_boss_outfit = Enemy("Gordon Goblin", "Warrior", "Male", 1, 25, 25, 1, 0, 0, 25, 25, 25, 0, 500, 100, "Enemy",
                              0, [axe_outfit], 0, 0, 87, 110, ['img/characters/bosses/blodister_boss_outfit.png'], False,
                              True)

""" Random Monsters """
goblin1_outfit = Enemy("Gordon Goblin", "Warrior", "Male", 1, 25, 25, 1, 0, 0, 25, 25, 25, 0, 500, 100, "Enemy", 0,
                       [axe_outfit], 0, 0, 32, 32, ['img/characters/random_enemies/goblin1_outfit.png'], False, True)
# firefly1_outfit = Enemy("Gordon Goblin","Warrior","Male",1,25,25,1,0,0,25,25,25,0,500,100,"Boss",0,[axe_outfit],0,0,32,32,['img/characters/random_enemies/firefly_outfit(1).png'],False,False)
# firefly2_outfit = Enemy("Gordon Goblin","Warrior","Male",1,25,25,1,0,0,25,25,25,0,500,100,"Boss",0,[axe_outfit],0,0,32,32,['img/characters/random_enemies/firefly_outfit(2).png'],False,False)

""" Crucials(Elites) """
jadugara_outfit = Enemy("Gordon Goblin", "Warrior", "Male", 1, 25, 25, 1, 0, 0, 25, 25, 25, 0, 500, 100, "Enemy", 0,
                        [axe_outfit], 0, 0, 52, 92, ['img/characters/crucials/jadugara_outfit.png'], False, True)

attack_button = skill_Attack(600,40,200,40,False,True,"info","Attack")
off_abilities_button = move_Button(600,120,200,40,False,True,"info","OffAbilities")
step_button = move_Button(600, 40, 200, 40, False, True, "info", "Step")
def_abilities_button = move_Button(600, 120, 200, 40, False, True, "info", "DefAbilities")

"""                                                 Basic variables arrays                                          """
# enemies = [blodister_boss_outfit, firefly1_outfit, firefly2_outfit, gardon_boss_outfit, goblin1_outfit, jadugara_outfit]
enemies = [blodister_boss_outfit, gardon_boss_outfit, goblin1_outfit, jadugara_outfit]

axes = [axe_outfit]
""" Boots """
boots = [boots_outfit]
""" Bows """
bows = [bow_outfit]
""" Chests """
chests = [chest_outfit]
""" Gloves """
gloves = [gloves_outfit]
""" Hammers """
hammers = [hammer_outfit]
""" Helmets """
helmets = [urand_pondering_helmet_outfit]
""" Knifes """
knifes = [knife_outfit]
""" Maces """
maces = [mace_outfit]
""" Necklets """
necklets = [necklet_outfit]
""" Rings """
rings = [moonstone_ring_outfit]
""" Shields """
shields = [large_shield_outfit]
""" Staffs """
staffs = [staff_outfit]
""" Swords """
swords = [sword_outfit]
""" Potions """
potions = [potion_outfit]

"""                                             INTERFACES PACKETS                                                  """

main_intreface_buttons = [new_game_button, load_game_button, monster_img_int1, monster2_img_int1, monster3_img_int1]
game_interface_buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                          show_stats_button, console_button, achivements_button, abilities_button,
                          antimatter_cavity_button, arena_button, daily_lucky_button, fusion_side_button,
                          theunderworld_button]


def game_interface_text():
    game_interface_text = [
        Text(1280 - 170 - math.floor(len(my_character.name) * 3), 250, str(my_character.name), 18, "name_lvl_proff"),
        Text(1280 - 170 - math.floor(len(str(my_character.lvl)) * 3), 270, str(my_character.lvl), 18, "name_lvl_proff"),
        Text(1280 - 170 - math.floor(len(my_character.profession) * 3), 290, str(my_character.profession), 18,
             "name_lvl_proff")]
    return game_interface_text



background = bg_1
buttons = main_intreface_buttons
texts = []
add_events = []

def get_background():
    return background


def get_buttons():
    return buttons


def get_texts():
    return texts


def get_add_events():
    return add_events


def set_background(new_background):
    global background
    background = new_background


def set_buttons(new_buttons):
    global buttons
    buttons = new_buttons


def set_texts(new_texts):
    global texts
    texts = new_texts


def set_add_events(new_add_events):
    global add_events
    add_events = new_add_events


def get_my_character():
    return my_character


def set_my_character(new_my_character):
    global my_character
    my_character = new_my_character


def get_cursor():
    return cursor

def check_mouse_position(arrElements):
    mpos = pygame.mouse.get_pos()
    try:
        for bt in arrElements:
            if mpos[0] > bt.x and mpos[0] < bt.x + bt.width and mpos[1] > bt.y and mpos[
                1] < bt.y + bt.height:
                if bt.able_press:
                    if bt.changeable:
                        bt.change = True
                    if pygame.mouse.get_pressed()[0] == 1:
                        print(str(bt.x))
                        bt.onclick()
            else:
                if bt.changeable:
                    bt.change = False
    except Exception as e:
        raise e
        # print("{}: {}".format(e.__class__.__name__,e))

"""                                               Button Functions                                                  """

""" Menu Icons """


def print_bug_log(type_of_bug):
    raport = Text(0, 0, f"Button '{type_of_bug}' doesn't work! Inform me about it: ", 10, "fight")
    return raport


def show_stats_button_onclick():
    _background = get_background()
    _buttons = get_buttons()
    _texts = get_texts()
    _my_character = get_my_character()
    if stats_panel in _buttons:
        text_arr = [text_a for text_a in _texts if text_a.type == "statistics"]
        for text_a in text_arr:
            _texts.remove(text_a)
        _buttons.remove(stats_panel)
    else:
        _buttons.append(stats_panel)
        text = []
        for i, stat in enumerate(_my_character.stats):
            text.append(
                Text(_background.width - eqandcharacter_panel.width - stats_panel.width + 120, 18 * i + 75, str(stat),
                     14, "statistics"))
        for text_b in text:
            _texts.append(text_b)
    set_buttons(_buttons)
    set_texts(_texts)


def quests_button_onclick():
    _buttons = get_buttons()
    if quests_panel in _buttons:
        _buttons.remove(quests_panel)
    else:
        _buttons.append(quests_panel)
    set_buttons(_buttons)


def raportbug_button_onclick():
    try:
        raport_bug()
    except:
        chat_panel.get_text(print_bug_log("Bug Raport"))


def console_button_onclick():
    import console
    console.console()


""" Shop """


def fusion_side_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopaxes_button,
                shopboots_button, shopbows_button, shopchests_button, shopgloves_button,
                shophammers_button, shophelmets_button, shopknifes_button, shopmaces_button, shopnecklets_button,
                shoppotions_button, shoprings_button, shopshields_button, shopstaffs_button, shopswords_button,
                close_button]
    set_buttons(_buttons)


def shop_axes_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopaxes_panel,
                close_button, axe_outfit]
    set_buttons(_buttons)


def shop_boots_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopboots_panel, close_button,
                boots_outfit]
    set_buttons(_buttons)


def shop_bows_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopbows_panel, close_button,
                bow_outfit]
    set_buttons(_buttons)


def shop_chests_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopchests_panel, close_button,
                chest_outfit]
    set_buttons(_buttons)


def shop_gloves_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopgloves_panel, close_button,
                gloves_outfit]
    set_buttons(_buttons)


def shop_hammers_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shophammers_panel,
                close_button, hammer_outfit]
    set_buttons(_buttons)


def shop_helmets_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shophelmets_panel,
                close_button, urand_pondering_helmet_outfit]
    set_buttons(_buttons)


def shop_knifes_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopknifes_panel, close_button,
                knife_outfit]
    set_buttons(_buttons)


def shop_maces_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopmaces_panel, close_button,
                mace_outfit]
    set_buttons(_buttons)


def shop_necklets_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopnecklets_panel,
                close_button, necklet_outfit]
    set_buttons(_buttons)


def shop_potions_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shoppotions_panel,
                close_button, potion_outfit]
    set_buttons(_buttons)


def shop_rings_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shoprings_panel, close_button,
                moonstone_ring_outfit]
    set_buttons(_buttons)


def shop_shields_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopshields_panel,
                close_button, large_shield_outfit]
    set_buttons(_buttons)


def shop_staffs_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopstaffs_panel, close_button,
                staff_outfit]
    set_buttons(_buttons)


def shop_swords_button_onclick():
    _buttons = [chat_panel, eqandcharacter_panel, save_button, raportbug_button, quests_button,
                show_stats_button, console_button, achivements_button, abilities_button, shopswords_panel, close_button,
                sword_outfit]
    set_buttons(_buttons)


""" Battle """


def antimatter_cavity_button_onclick():
    fight = Fight()
    _add_events = get_add_events()
    _add_events.append(fight)
    set_add_events(_add_events)


def new_game_button_onclick():
    set_background(bg_2)
    set_buttons([])
    set_texts([])
    set_add_events([])
    ret = login_menu()
    if ret:
        set_my_character(move_to_my_character(My_character))
        set_background(bg_1)
        set_buttons(game_interface_buttons)
        set_texts(game_interface_text())
    else:
        set_background(bg_1)
        set_buttons(main_intreface_buttons)
        set_texts([])


def load_game_button_onclick():  # TODO
    set_background(bg_2)
    set_buttons([])
    set_texts([])
    set_add_events([])


def close_button_onclick():
    set_buttons(game_interface_buttons)

setattr(show_stats_button, "onclick", show_stats_button_onclick)
setattr(quests_button, "onclick", quests_button_onclick)
setattr(raportbug_button, "onclick", raportbug_button_onclick)
setattr(fusion_side_button, "onclick", fusion_side_button_onclick)
setattr(antimatter_cavity_button, "onclick", antimatter_cavity_button_onclick)
setattr(new_game_button, "onclick", new_game_button_onclick)
setattr(load_game_button, "onclick", load_game_button_onclick)
setattr(shopaxes_button, "onclick", shop_axes_button_onclick)
setattr(shopboots_button, "onclick", shop_boots_button_onclick)
setattr(shopbows_button, "onclick", shop_bows_button_onclick)
setattr(shopchests_button, "onclick", shop_chests_button_onclick)
setattr(shopgloves_button, "onclick", shop_gloves_button_onclick)
setattr(shophammers_button, "onclick", shop_hammers_button_onclick)
setattr(shophelmets_button, "onclick", shop_helmets_button_onclick)
setattr(shopknifes_button, "onclick", shop_knifes_button_onclick)
setattr(shopmaces_button, "onclick", shop_maces_button_onclick)
setattr(shopnecklets_button, "onclick", shop_necklets_button_onclick)
setattr(shoppotions_button, "onclick", shop_potions_button_onclick)
setattr(shoprings_button, "onclick", shop_rings_button_onclick)
setattr(shopshields_button, "onclick", shop_shields_button_onclick)
setattr(shopstaffs_button, "onclick", shop_staffs_button_onclick)
setattr(shopswords_button, "onclick", shop_swords_button_onclick)
setattr(console_button, "onclick", console_button_onclick)
setattr(close_button, "onclick", close_button_onclick)