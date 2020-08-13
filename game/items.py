class Item():
    """ The base information for all items """
    # Constructor

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

        def __str__(self):
            return "{self.name}\n=====\n{self.description}\nValue: {self.value}\n"


class Gold(Item):
    """ Subclass of Item """
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Gold",
                         description=f"A Round Coin With {self.amount} stamped on the front.",
                         value=self.amount)

