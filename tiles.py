import items, enemies, actions, world


class MapTile:
    """ Create World """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Warning if a MapTile is created directly
    def intro_text(self):
        """Information to be displayed when the player moves into this tile."""
        raise NotImplementedError()

    def modify_player(self, player):
        """Process actions that change the state of the player."""
        raise NotImplementedError()

    def adjacent_moves(self):
        """ Returns all move actions for adjacent tiles """
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveLeft())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveRight())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveUp())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveDown())

        return moves

    def available_actions(self):
        """ Returns all of the available actions on current tile """
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    """ Start Tile """

    def intro_text(self):
        return """
    You find yourself in a forest with the sun high in the sky.
    You can make out four paths, each showing a way out of the clearing """

    def modify_player(self, player):
        # Room has no action on player
        pass


class ExitRoom(MapTile):
    def intro_text(self):
        return """
        You keep walking until you notice a sign that points to the nearest town. 
        You start making a mad dash to civilization. """

    def modify_player(self, player):
        player.victory = True


class EmptyBeachPath(MapTile):
    def intro_text(self):
        return """
        You find yourself on an empty beach. You find footprints in the sand and follow them.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class EmptyDesertPath(MapTile):
    def intro_text(self):
        return """
        You find yourself faced with a mountain of sand as you make way up.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class EmptySnowPath(MapTile):
    def intro_text(self):
        return """
        You see breath as you protect yourself from the cold and march forwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class EmptyForestPath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the forest. You keep going foward.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    """ Loot Tile """

    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)


class FindGoodRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold())

    def intro_text(self):
        return """
        You find some coins. Better keep them safe.
        """


class FindCrystalsRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Crystals())

    def intro_text(self):
        return """
        You find a rare crystal. Better keep it safe.
        """


class FindGlovesRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gloves())

    def intro_text(self):
        return """
        You find a nice pair of gloves.
        """


class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Sword())

    def intro_text(self):
        return """
        You find a nice looking wood sword. Hopeful it will protect you.
        """


class FindDraggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dragger())

    def intro_text(self):
        return """
        A weapon where you have to be close and personal.
        """


class FindAxeRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Axe())

    def intro_text(self):
        return """
        Always aim for the head.
        """


class FindNightSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.NightSword())

    def intro_text(self):
        return """
        Best Sword. You find it.
        """


class EnemyRoom(MapTile):
    """ Enemy Tile """

    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(
                f"Enemy does {self.enemy.damage}. You have {self.player.hp} HP remaining ")

    def available_actions(self):
        if self.enemy.is_action():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class FellwoodSpectre(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.FellwoodSpectre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A spectre appears behind you and attempts to slash at you.
            """
        else:
            return """
            The surronding area is empty of any spectres.
            """


class StormGhoul(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.StormGhoul())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A demon like monster cloaked in electricity.
            """
        else:
            return """
            The dead body of the ghoul is resting on the ground.
            """


class DreadFiend(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.DreadFiend())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A monster with bones sticking out of all its body parts attacks you.
            """
        else:
            return """
            The monster lays on the ground motionless.
            """


class ScarletHydra(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ScarletHydra())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A monster cloaked in fire with multiple heads attack you.
            """
        else:
            return """
            The monster lays on the motionless as several heads are missing.
            """
