import random
import items
import world
from termcolor import colored
from colorama import init
init()


class Player():
    """ The base class for player """

    def __init__(self):
        self.inventory = [items.Gold(15), items.Crystals(1), items.Gloves()]
        self.hp = 150
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        """ Print Out Current Inventory """
        for item in self.inventory:
            print(colored(item, color='cyan'), '\n')

    def move(self, dx, dy):
        """ Player Moves Around The Map """
        self.location_x += dx
        self.location_y += dy
        print(colored(world.tile_exists(self.location_x,
                                        self.location_y).intro_text(), color='green'))

    def move_up(self):
        self.move(dx=0, dy=-1)

    def move_down(self):
        self.move(dx=0, dy=1)

    def move_left(self):
        self.move(dx=1, dy=0)

    def move_right(self):
        self.move(dx=-1, dy=0)

    def quit_game(self):
        print(colored("You Have Quit The Game", color="red"))
        return quit()

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        print(
            colored(f"\nYou use {best_weapon.name} against {enemy.name}.", color="green"))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print(colored(f"\nYou killed {enemy.name}.\n", color='green'))
        else:
            print(colored(f"\n{enemy.name} HP is {enemy.hp}.", color='red'))

    def flee(self, tile):
        """ Moves the player randomly to an adjacent tile """
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
