import player

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return f"{self.hotkey}: {self.name}"


class MoveUp(Action):
    def __init__(self):
        super().__init__(
            method=Player.move_up,
            name='Move North',
            hotkey='w')


class MoveRight(Action):
    def __init__(self):
        super().__init__(
            method=Player.move_right,
            name='Move East',
            hotkey='d')


class MoveDown(Action):
    def __init__(self):
        super().__init__(
            method=Player.move_down,
            name='Move South',
            hotkey='s')


class MoveLeft(Action):
    def __init__(self):
        super().__init__(
            method=Player.move_left,
            name='Move West',
            hotkey='a')


class ViewInventory(Action):
    """ Prints The Player's Inventory """

    def __init__(self):
        super().__init__(
            method=Player.print_inventory,
            name='View Inventory',
            hotkey="i")


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(
            method=Player.attack,
            name="Attack",
            hotkey="a",
            enemy=enemy)


class Flee(Action):
    def __init__(self, tile):
        super().__init__(
            method=Player.flee,
            name="Flee",
            hotkey="f",
            tile=tile)
