from entities.initial_screen_entity import StartScreen
import pygame
from util.change_window_size_util import change_window_size
from util.update_coords import update_coords
from entities.item_entity import Item
from entities.inventory_entity import Inventory

GAME_TITLE = "Crew"


class Crew(object):
    def __init__(self):
        self.screen = None
        self.screen_size = None
        self.clock = None
        self.current_screen = None

    def init(self):
        pygame.init()

        info = pygame.display.Info()  # Tem que ser antes do .set_mode()
        self.screen_dimensions = (info.current_w, info.current_h)

        self.screen = pygame.display.set_mode(
            (self.screen_dimensions[0] / 2, self.screen_dimensions[1] / 2),
            pygame.RESIZABLE,
        )
        self.window_dimensions = self.screen.get_size()
        is_fullscreen = False

        self.clock = pygame.time.Clock()
        self.current_screen = StartScreen(self.window_dimensions)

        pygame.display.set_caption(GAME_TITLE)

        if self.window_dimensions[1] * 2 < self.window_dimensions[0]:
            track_left_coord = (
                self.window_dimensions[0] // 2 - self.window_dimensions[1] // 2
            )
            track_right_coord = track_left_coord + self.window_dimensions[1]
            track_bottom_coord = self.window_dimensions[1]
        else:
            track_left_coord = self.window_dimensions[0] // 4
            track_right_coord = 3 * self.window_dimensions[0] // 4
            track_bottom_coord = self.window_dimensions[0] // 2

        track_coords = (
            track_left_coord,
            0,
            track_right_coord,
            track_bottom_coord,
        )  # left, top, right, bottom

        player_coords = (
            (track_coords[2] - track_coords[0]) // 2,
            track_coords[1] - (track_coords[2] - track_coords[0]) / 5,
            None,
            None,
        )  # left, top, right, bottom

        propellant_coords = (
            0,
            0,
            None,
            None,
        )  # left, top, right, bottom

        bullet_coords = (
            0,
            0,
            None,
            None,
        )  # left, top, right, bottom

        comet_coords = (
            0,
            0,
            None,
            None,
        )  # left, top, right, bottom

        inventory = Inventory()

        # Add items to the inventory with custom positions
        item1 = Item("Item 1", (50, 50))
        item2 = Item("Item 2", (50, 350))
        # Add another "Item 1" to test quantity stacking
        item3 = Item("Item 3", (50, 500))
        item4 = Item("Item 4", (700, 450))
        item5 = Item("Item 5", (700, 50))
        inventory.add_item(item1)
        inventory.add_item(item2)
        inventory.add_item(item3)
        inventory.add_item(item4)
        inventory.add_item(item5)

        is_running = True
        while is_running:
            (self.window_dimensions,
                track_coords,
                background,
                asteroid,
                asteroid_dimensions,
                asteroid_left_coord,
                player,
                player_dimensions,
                player_new_coords,
                propellant,
                propellant_dimensions,
                propellant_new_coords,
                bullet,
                bullet_dimensions,
                bullet_new_coords,
                comet,
                comet_dimensions,
                comet_new_coords,
             ) = change_window_size(
                self.screen,
                track_coords,
                player_coords,
                propellant_coords,
                bullet_coords,
                comet_coords,
            )

            player_coords = update_coords(player_coords, player_new_coords)
            propellant_coords = update_coords(
                propellant_coords, propellant_new_coords)
            bullet_coords = update_coords(bullet_coords, bullet_new_coords)
            comet_coords = update_coords(comet_coords, comet_new_coords)

            asteroid_coords = (
                asteroid_left_coord,
                None,
                None,
                None,
            )  # left, top, right, bottom

            self.screen.blit(background, (0, 0))
            self.screen.blit(player, (player_coords[0], player_coords[1]))

            asteroid_coords = update_coords(
                asteroid_coords, (None, 0, None, None))
            while asteroid_coords[1] < self.window_dimensions[1]:
                self.screen.blit(
                    asteroid, (asteroid_coords[0], asteroid_coords[1]))
                self.screen.blit(
                    asteroid,
                    (
                        asteroid_coords[0]
                        + track_coords[2]
                        - track_coords[0]
                        + asteroid_dimensions[1],
                        asteroid_coords[1],
                    ),
                )
                asteroid_coords = update_coords(
                    asteroid_coords,
                    (None, asteroid_coords[1] +
                     asteroid_dimensions[1], None, None),
                )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    if not is_fullscreen:
                        self.screen = pygame.display.set_mode(
                            (self.screen_dimensions[0],
                             self.screen_dimensions[1]),
                            pygame.FULLSCREEN,
                        )
                        is_fullscreen = True
                    else:
                        self.screen = pygame.display.set_mode(
                            (
                                self.screen_dimensions[0] // 2,
                                self.screen_dimensions[1] // 2,
                            ),
                            pygame.RESIZABLE,
                        )
                        is_fullscreen = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    is_running = False
                self.current_screen = self.current_screen.run(
                    self.screen, self.window_dimensions, event)
