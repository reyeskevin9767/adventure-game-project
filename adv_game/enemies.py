class Enemy:
    """ Basic Info About Enemy"""

    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class FellwoodSpectre(Enemy):
    """ Info About Fellwood Spectre"""

    def __init__(self):
        super().__init__(
            name="Fellwood Spectre",
            hp=10,
            damage=5)


class StormGhoul(Enemy):
    """ Info About Storm Ghoul"""

    def __init__(self):
        super().__init__(
            name="Storm Ghoul",
            hp=20,
            damage=10)


class DreadFiend(Enemy):
    """ Info ABout Dread Fiend"""

    def __init__(self):
        super().__init__(
            name="Dread Fiend",
            hp=40,
            damage=20)


class ScarletHydra(Enemy):
    """ Info ABout Scarlet Hydra"""

    def __init__(self):
        super().__init__(
            name="Scarlet Hydra",
            hp=60,
            damage=30)
