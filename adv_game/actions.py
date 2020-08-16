from player import Player


class Action():
    """ The base class for all actions """

    def __init__(self, method, name, hotkey, **kwargs):
        """ Creates a new action """
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return f"{self.hotkey}: {self.name}"


class MoveUp(Action):
    """ Move North """
    def __init__(self):
        super().__init__(
            method=Player.move_up,
            name='Move North',
            hotkey='w')


class MoveLeft(Action):
    """ Move East """
    def __init__(self):
        super().__init__(
            method=Player.move_left,
            name='Move East',
            hotkey='d')


class MoveDown(Action):
    """ Move South """
    def __init__(self):
        super().__init__(
            method=Player.move_down,
            name='Move South',
            hotkey='s')


class MoveRight(Action):
    """ Move West """
    def __init__(self):
        super().__init__(
            method=Player.move_right,
            name='Move West',
            hotkey='a')

class QuitGame(Action):
    """ Exit Game """
    def __init__(self):
        super().__init__(
            method=Player.quit_game,
            name='Quit Game',
            hotkey='q')


class ViewInventory(Action):
    """ Prints The Player's Inventory """

    def __init__(self):
        super().__init__(
            method=Player.print_inventory,
            name='View Inventory',
            hotkey="i")


class Attack(Action):
    """ Attack Enemy """
    def __init__(self, enemy):
        super().__init__(
            method=Player.attack,
            name="Attack",
            hotkey="a",
            enemy=enemy)


class Flee(Action):
    def __init__(self, tile):
        """ Free From Enemy """
        super().__init__(
            method=Player.flee,
            name="Flee",
            hotkey="f",
            tile=tile)
