#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_OPTION, C_WHITE, C_BLUE, C_BLACK


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        self.player1_surf = pygame.image.load('./asset/Player1Menu.png').convert_alpha()
        self.player1_rect = self.player1_surf.get_rect(left=450, top=325)

        self.player2_surf = pygame.image.load('./asset/Player2Menu.png').convert_alpha()
        self.player2_rect = self.player2_surf.get_rect(left=450, top=370)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(120, "Forest Wizard", C_BLUE, ((WIN_WIDTH / 2), 120))
            self.menu_text(40, "SELECT YOUR PLAYER:", C_BLACK, ((WIN_WIDTH / 2), 300))
            self.window.blit(self.player1_surf, self.player1_rect)
            self.window.blit(self.player2_surf, self.player2_rect)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i], C_BLACK, ((WIN_WIDTH / 2), 345 + 45 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 345 + 45 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
