import random
import items
import world


class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        print(f"You use {best_weapon.name} against {enemy.name}.")
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print(f"You killed {enemy.name}.")
        else:
            print(f"{enemy.name} HP is {enemy.hp}")

    def flee(self, tile):
        """ Moves the player randomly to an adjacent tile """
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])