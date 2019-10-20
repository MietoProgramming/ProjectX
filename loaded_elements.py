from basic_class import *

"""                                                 Backgrounds                                                     """

bg_0 = Background('img/gui/backgrounds/blackbackground.png')
bg_1 = Background('img/gui/backgrounds/game_background.png')
bg_2 = Background('img/gui/backgrounds/Loadingbackground1.png')

fightbackground_desert1 = Button(414, 0, 530, 720, ['img/gui/backgrounds/fightbackground_desert1_new.png'], False,
                                 False, "whatever", "INFO")
fightbackground_desert2 = Button(414, 0, 750, 720, ['img/gui/backgrounds/fightbackground_desert2.png'], False, False,
                                 "whatever", "INFO")

"""                    Button(x, y, width, height, images, changeable, able_press, typeofinfo, info)                """

"""       Interface 1           """
new_game_button = Button(492, 300, 296, 80,
                         ['img/gui/buttons/new_game_button.png', 'img/gui/buttons/new_game_button_hover.png'], True,
                         True, "whatever", "INFO")
load_game_button = Button(492, 500, 296, 80,
                          ['img/gui/buttons/load_game_button.png', 'img/gui/buttons/load_game_button_hover.png'], True,
                          False, "whatever", "INFO")
monster_img_int1 = Button(522, 0, 237, 300, ['img/gui/panels/blodister_boss_outfit_main_interface.png'], False, True,
                          "whatever", "INFO")
monster2_img_int1 = Button(110, 300, 369, 312, ['img/gui/panels/ghostinstance_2_main_interface.png'], False, True,
                           "whatever", "INFO")
monster3_img_int1 = Button(801, 300, 369, 312, ['img/gui/panels/ghostinstance_2_main_interface.png'], False, True,
                           "whatever", "INFO")

"""       Interface 3         """

""" Chat Panel """
chat_panel = Chat(0, 0, 414, 720, ['img/gui/panels/chat_panel.png'], False, False, "whatever", "INFO")

""" Mid Panel """
antimatter_cavity_button = Button(450, 10, 250, 99, ['img/gui/buttons/antimatter_cavity_button.png',
                                                     'img/gui/buttons/antimatter_cavity_button_hover.png'], True,
                                  True, "whatever", "INFO")
arena_button = Button(450, 160, 250, 99,
                      ['img/gui/buttons/arena_button.png', 'img/gui/buttons/arena_button_hover.png'], True, False,
                      "whatever", "INFO")

daily_lucky_button = Button(450, 310, 250, 99,
                            ['img/gui/buttons/daily_lucky_button.png', 'img/gui/buttons/daily_lucky_button_hover.png'],
                            True, False, "whatever", "INFO")
fusion_side_button = Button(450, 460, 250, 99,
                            ['img/gui/buttons/fusion_side_button.png', 'img/gui/buttons/fusion_side_button_hover.png'],
                            True, True, "whatever", "INFO")
theunderworld_button = Button(450, 610, 250, 99, ['img/gui/buttons/theunderworld_button.png',
                                                  'img/gui/buttons/theunderworld_button_hover.png'], True, False,
                              "whatever", "INFO")
buy_button = Button(450, 400, 250, 99, ['img/gui/buttons/buy_button.png', 'img/gui/buttons/buy_button_hover.png'],
                    True, True, "whatever", "INFO")
shopaxes_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopaxes_panel.png'], False, False, "whatever", "INFO")
shopboots_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopboots_panel.png'], False, False, "whatever", "INFO")
shopbows_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopbows_panel.png'], False, False, "whatever", "INFO")
shopchests_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopchests_panel.png'], False, False, "whatever", "INFO")
shopgloves_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopgloves_panel.png'], False, False, "whatever", "INFO")
shophammers_panel = Button(506, 50, 345, 600, ['img/gui/panels/shophammers_panel.png'], False, False, "whatever",
                           "INFO")
shophelmets_panel = Button(506, 50, 345, 600, ['img/gui/panels/shophelmets_panel.png'], False, False, "whatever",
                           "INFO")
shopknifes_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopknifes_panel.png'], False, False, "whatever", "INFO")
shopmaces_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopmaces_panel.png'], False, False, "whatever", "INFO")
shopnecklets_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopnecklets_panel.png'], False, False, "whatever",
                            "INFO")
shoprings_panel = Button(506, 50, 345, 600, ['img/gui/panels/shoprings_panel.png'], False, False, "whatever", "INFO")
shopshields_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopshields_panel.png'], False, False, "whatever",
                           "INFO")
shopstaffs_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopstaffs_panel.png'], False, False, "whatever", "INFO")
shopswords_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopswords_panel.png'], False, False, "whatever", "INFO")
shoppotions_panel = Button(506, 50, 345, 600, ['img/gui/panels/shopswords_panel.png'], False, False, "whatever", "INFO")
shoppotions_button = Button(506, 50, 126, 50, ['img/gui/buttons/shop_potions_button.png',
                                               'img/gui/buttons/shop_potions_button_hover.png'], True, True, "whatever",
                            "INFO")
shopaxes_button = Button(506, 120, 126, 50, ['img/gui/buttons/shop_axes_button.png',
                                             'img/gui/buttons/shop_axes_button_hover.png'], True, True, "whatever",
                         "INFO")
shopboots_button = Button(506, 190, 126, 50, ['img/gui/buttons/shop_boots_button.png',
                                              'img/gui/buttons/shop_boots_button_hover.png'], True, True, "whatever",
                          "INFO")
shopbows_button = Button(506, 260, 126, 50, ['img/gui/buttons/shop_bows_button.png',
                                             'img/gui/buttons/shop_bows_button_hover.png'], True, True, "whatever",
                         "INFO")
shopchests_button = Button(506, 330, 126, 50, ['img/gui/buttons/shop_chests_button.png',
                                               'img/gui/buttons/shop_chests_button_hover.png'], True, True, "whatever",
                           "INFO")
shopgloves_button = Button(506, 400, 126, 50, ['img/gui/buttons/shop_gloves_button.png',
                                               'img/gui/buttons/shop_gloves_button_hover.png'], True, True, "whatever",
                           "INFO")
shophammers_button = Button(506, 470, 126, 50, ['img/gui/buttons/shop_hammers_button.png',
                                                'img/gui/buttons/shop_hammers_button_hover.png'], True, True,
                            "whatever", "INFO")
shophelmets_button = Button(506, 540, 126, 50, ['img/gui/buttons/shop_helmets_button.png',
                                                'img/gui/buttons/shop_helmets_button_hover.png'], True, True,
                            "whatever", "INFO")
shopknifes_button = Button(724, 50, 126, 50, ['img/gui/buttons/shop_knifes_button.png',
                                              'img/gui/buttons/shop_knifes_button_hover.png'], True, True, "whatever",
                           "INFO")
shopmaces_button = Button(724, 120, 126, 50, ['img/gui/buttons/shop_maces_button.png',
                                              'img/gui/buttons/shop_maces_button_hover.png'], True, True, "whatever",
                          "INFO")
shopnecklets_button = Button(724, 190, 126, 50, ['img/gui/buttons/shop_necklets_button.png',
                                                 'img/gui/buttons/shop_necklets_button_hover.png'], True, True,
                             "whatever", "INFO")
shoprings_button = Button(724, 260, 126, 50, ['img/gui/buttons/shop_rings_button.png',
                                              'img/gui/buttons/shop_rings_button_hover.png'], True, True, "whatever",
                          "INFO")
shopshields_button = Button(724, 330, 126, 50, ['img/gui/buttons/shop_shields_button.png',
                                                'img/gui/buttons/shop_shields_button_hover.png'], True, True,
                            "whatever", "INFO")
shopstaffs_button = Button(724, 400, 126, 50, ['img/gui/buttons/shop_staffs_button.png',
                                               'img/gui/buttons/shop_staffs_button_hover.png'], True, True, "whatever",
                           "INFO")
shopswords_button = Button(724, 470, 126, 50, ['img/gui/buttons/shop_swords_button.png',
                                               'img/gui/buttons/shop_swords_button_hover.png'], True, True, "whatever",
                           "INFO")

""" Right Panel """
eqandcharacter_panel = Button(945, 0, 335, 720, ['img/gui/panels/eqandcharacter_panel.png'], False, False, "whatever",
                              "INFO")
quests_panel = Button(1280 - 335 - 345, 0, 345, 600, ['img/gui/panels/quests_panel.png'], False, True, "whatever",
                      "INFO")
quests_button = Button(1005, 400, 24, 24, ['img/gui/buttons/quests_button.png'], False, True, "whatever", "INFO")
raportbug_button = Button(1076, 400, 24, 24, ['img/gui/buttons/raportbug_button.png'], False, True, "whatever", "INFO")
save_button = Button(1127, 400, 24, 24, ['img/gui/buttons/save2_button.png'], False, True, "whatever", "INFO")
achivements_button = Button(1041, 400, 24, 24, ['img/gui/buttons/achivements_button.png'], False, True, "whatever",
                            "INFO")
abilities_button = Button(1159, 400, 24, 24, ['img/gui/buttons/abilities_button.png'], False, True, "whatever", "INFO")
console_button = Button(1191, 400, 24, 24, ['img/gui/buttons/console_button.png'], False, True, "whatever", "INFO")
show_stats_button = Button(995, 25, 31, 31,
                           ['img/gui/buttons/show_stats_button.png', 'img/gui/buttons/show_stats_button_hover.png'],
                           True, True, "whatever", "INFO")
stats_panel = Button(760, 0, 185, 600, ['img/gui/panels/stats_panel.png'], False, False, "whatever", "INFO")
close_button = Button(1280 - 335 - 48, 0, 48, 48,
                      ['img/gui/buttons/close_button.png', 'img/gui/buttons/close_button_hover.png'],
                      True, True, "whatever", "INFO")

""" Fight Panel """
accept_button = Button(500, 400, 300, 200, ['img/gui/buttons/accept_button.png'], True, True, "whatever", "INFO")
deny_button = Button(500, 400, 300, 200, ['img/gui/buttons/deny_button.png'], True, True, "whatever", "INFO")
hpandmana_panel = Button(0, 0, 0, 0, ['img/gui/panels/hpandmana_panel.png'], False, True, "whatever", "INFO")
drop_panel = Button(0, 0, 0, 0, ['img/gui/panels/drop_panel.png'], False, True, "whatever", "INFO")
win_character = Button(0, 0, 0, 0, ['img/characters/mycharacters/warrior_front.png'], False, False, "whatever", "INFO")
move_in_battle_panel = Button(430, 10, 495, 234, ['img/gui/panels/move_in_battle_panel.png'], False, False, "whatever",
                              "INFO")

"""                                                   Items                                                         """

""" Axes """
axe_outfit = Item(['img/items/Axes/broad_axe_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15,
                  crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Boots """
boots_outfit = Item(['img/items/Boots/boots_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15,
                    crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Bows """
bow_outfit = Item(['img/items/Bows/bow_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15, crit_hit=10,
                  dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Chests """
chest_outfit = Item(['img/items/Chests/chain_mail_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15,
                    crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Gloves """
gloves_outfit = Item(['img/items/Gloves/gloves_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15,
                     crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Hammers """
hammer_outfit = Item(['img/items/Hammers/hammer_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15,
                     crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Helmets """
urand_pondering_helmet_outfit = Item(['img/items/Helmets/urand_pondering_helmet_outfit.png'], "Axe", 500, "Warrior",
                                     "Weapon", 1, addstrength=15, crit_hit=10, dmg=40, attack_speed=20,
                                     heal_per_attack=5, x=555, y=100)
""" Knifes """
knife_outfit = Item(['img/items/Knifes/knife_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15,
                    crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Maces """
mace_outfit = Item(['img/items/Maces/mace_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15, crit_hit=10,
                   dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Necklets """
necklet_outfit = Item(['img/items/Necklets/necklet_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15,
                      crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Rings """
moonstone_ring_outfit = Item(['img/items/Rings/moonstone_ring_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1,
                             addstrength=15, crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Shields """
large_shield_outfit = Item(['img/items/Shields/large_shield_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1,
                           addstrength=15, crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Staffs """
staff_outfit = Item(['img/items/Staffs/staff_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15,
                    crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Swords """
sword_outfit = Item(['img/items/Swords/sword_outfit.png'], "Axe", 500, "Warrior", "Weapon", 1, addstrength=15,
                    crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)
""" Potions """
potion_outfit = Item(['img/items/Potions/potion_golden.png'], "Axe", 500, "Warrior", "Potion", 1, addstrength=15,
                     crit_hit=10, dmg=40, attack_speed=20, heal_per_attack=5, x=555, y=100)

"""                                                 Characters                                                      """

""" My characters"""
warrior_outfit = ['img/characters/mycharacters/warrior_front.png', 'img/characters/mycharacters/warrior_back.png']
archer_outfit = ['img/characters/mycharacters/goblin_front.png', 'img/characters/mycharacters/goblin_back.png']
grave_my_character = ['img/characters/grave_my_character.png']
grave_enemy = ['img/characters/grave_enemy.png']



