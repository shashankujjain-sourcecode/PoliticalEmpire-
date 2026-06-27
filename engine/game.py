import pygame

import config

from ui.menu import MainMenu


class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode(
            (config.WIDTH, config.HEIGHT)
        )

        pygame.display.set_caption(config.TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        self.menu = MainMenu(self.screen)

    def run(self):

        while self.running:

            self.clock.tick(config.FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    self.running = False

                self.menu.handle_event(event)

            self.menu.draw()
