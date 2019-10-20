import pygame
from load import *

def catch_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run
            run = False
        _background = get_background()
        _buttons = get_buttons()
        _texts = get_texts()
        _add_events = get_add_events()
        check_mouse_position(_buttons)
        if _add_events != []:
            check_mouse_position([_add_events[0]])

def refresh():
    _background = get_background()
    _buttons = get_buttons()
    _texts = get_texts()
    _add_events = get_add_events()
    _cursor = get_cursor()
    _background.draw()
    for button in _buttons:
        button.draw()
    for text in _texts:
        text.draw()
    for event in _add_events:
        event.draw()
    window.blit(_cursor, (pygame.mouse.get_pos()))
    pygame.display.update()


clock = pygame.time.Clock()
while run:
    clock.tick(80)
    catch_event()
    refresh()
pygame.quit()