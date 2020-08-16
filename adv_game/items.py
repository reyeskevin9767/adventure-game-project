class Item():
    """ The base information for all items """

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

        def __str__(self):
            return "{self.name}\n=====\n{self.description}\nValue: {self.value}\n"


class Gold(Item):
    """ Info About Gold """

    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Gold",
                         description=f"A round coin with {self.amount} stamped on the front.",
                         value=self.amount)


class Crystals(Item):
    """ Info About Crystals """

    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Crystals",
                         description=f"A jagged rock with sharp edges worth {self.amount}.",
                         value=self.amount)


class Weapon(Item):
    """ The base information for all weapons """

    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

        def __str__(self):
            return f"{self.name}\n=====\nValue: {self.value}\nDamage: {self.damage}"


class Gloves(Weapon):
    """ Info About Gloves """

    def __init__(self):
        super().__init__(name="Gloves",
                         description="Regular pair of gloves. All its power comes from you.",
                         value=0,
                         damage=5)


class Sword(Weapon):
    """ Info About Sword """

    def __init__(self):
        super().__init__(name="Wood Sword",
                         description="A sword typically used for training. Better than using your fists.",
                         value=5,
                         damage=10)


class Dragger(Weapon):
    """ Info About Dragger """

    def __init__(self):
        super().__init__(name="Rusty Dragger",
                         description="A small dagger with some rust. Be better if you could throw the dragger.",
                         value=10,
                         damage=15)


class Axe(Weapon):
    """ Info About Axe """

    def __init__(self):
        super().__init__(name="Axe of Echo",
                         description="A weapon abandoned by a famous adventure. Pretty good axe.",
                         value=15,
                         damage=25)


class NightSword(Weapon):
    """ Info About NightSword """

    def __init__(self):
        super().__init__(name="Night's Edge",
                         description="A black sword with a snake style blade that deals deadly damage.",
                         value=25,
                         damage=35)
