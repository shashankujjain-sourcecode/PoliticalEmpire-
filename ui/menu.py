import pygame

import config


class MainMenu:

    def __init__(self, screen):

        self.screen = screen

        self.font = pygame.font.SysFont("arial", 50)

        self.small = pygame.font.SysFont("arial", 30)

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                pygame.event.post(
                    pygame.event.Event(pygame.QUIT)
                )

    def draw(self):

        self.screen.fill(config.BACKGROUND)

        title = self.font.render(
            "POLITICAL EMPIRE",
            True,
            config.WHITE
        )

        self.screen.blit(title, (360,120))

        text = self.small.render(
            "Press ESC to Exit",
            True,
            config.GREEN
        )

        self.screen.blit(text, (470,250))

        pygame.display.flip()
