import pygame
from util.values_global import SIZE_IMAGE_ITEM, ITEM_SPACING_INVENTORY_X_Y


class Life(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, SIZE_IMAGE_ITEM)
        self.rect = self.image.get_rect(topleft=position)
        self.player_life = 0

    def update(self, screen):
        screen.blit(self.image, self.rect)
