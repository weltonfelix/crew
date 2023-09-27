import pygame
from util.colors import WHITE, BLACK
from entities.credits_screen_entity import CreditsScreen

from entities.game_entity import Game

TEXT_COLOR = WHITE
BACKGROUND_COLOR = BLACK
FONT_SIZE = 48


class StartScreen(object):
    def __init__(self, screen_size):

        font = pygame.font.Font(None, FONT_SIZE)

        # Create text objects
        self._game_name = font.render("Crew", True, TEXT_COLOR)
        self._play_button = font.render("Play", True, TEXT_COLOR)
        self._credits_button = font.render("Credits", True, TEXT_COLOR)

        # Rectangles for buttons
        self._play_button_rect = self._play_button.get_rect(
            center=(screen_size[0] // 2, screen_size[1] // 2))
        self._credits_button_rect = self._credits_button.get_rect(
            center=(screen_size[0] // 2, screen_size[1] // 2 + 100))

    def draw(self, screen, screen_size):
        screen.fill(BACKGROUND_COLOR)

        # Draw text and buttons
        screen.blit(self._game_name, self._game_name.get_rect(
            center=(screen_size[0] // 2, screen_size[1] // 4)))
        screen.blit(self._play_button, self._play_button_rect)
        screen.blit(self._credits_button, self._credits_button_rect)
        pygame.display.flip()

    def run(self,screen, screen_size, event):
        is_visible = True
        if self._play_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_visible = False
                game = Game(screen_size)
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                return game
        elif self._credits_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_visible = False
                credits_screen = CreditsScreen(screen_size, self)
                return credits_screen
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

        if is_visible:
            self._play_button_rect = self._play_button.get_rect(
                center=(screen_size[0] // 2, screen_size[1] // 2))
            self._credits_button_rect = self._credits_button.get_rect(
                center=(screen_size[0] // 2, screen_size[1] // 2 + 100))

            self.draw(screen, screen_size)
        return self
