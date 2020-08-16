import unittest
from game.items import Item, Gold, Crystals, Weapon, Gloves, Sword, Dragger, Axe, NightSword

# * Testing Items


class BaseItemCases:
    class ItemTests(unittest.TestCase):
        """ Testing Item Template """

        def test_str(self):
            self.assertIsNotNone(str(self))


class GoldTests(BaseItemCases.ItemTests):
    """ Testing Gold Information And Amount """

    def setUp(self):
        self.gold = Gold(3)

    def test_init(self):
        self.assertEqual(self.gold.name, 'Gold')
        self.assertEqual(self.gold.description,
                         "A round coin with 3 stamped on the front.")
        self.assertEqual(self.gold.value, 3)


class CrystalsTests(BaseItemCases.ItemTests):
    """ Testing Crystals Information And Amount """

    def setUp(self):
        self.crystals = Crystals(1)

    def test_init(self):
        self.assertEqual(self.crystals.name, 'Crystals')
        self.assertEqual(self.crystals.description,
                         "A jagged rock with sharp edges worth 1.")
        self.assertEqual(self.crystals.value, 1)


class WeaponTests(BaseItemCases.ItemTests):
    """ Testing Weapon Template """

    def test_str(self):
        self.assertIsNotNone(str(self))


class GlovesWeaponTests(WeaponTests):
    """ Test Gloves Information And Damage """

    def setUp(self):
        self.gloves = Gloves()

    def test_init(self):
        self.assertEqual(self.gloves.name, 'Gloves')
        self.assertEqual(self.gloves.description,
                         'Regular pair of gloves. All its power comes from you.')
        self.assertEqual(self.gloves.value, 0)
        self.assertEqual(self.gloves.damage, 5)


class SwordWeaponTests(WeaponTests):
    """ Test Sword Information And Damage """

    def setUp(self):
        self.sword = Sword()

    def test_init(self):
        self.assertEqual(self.sword.name, 'Wood Sword')
        self.assertEqual(self.sword.description,
                         'A sword typically used for training. Better than using your fists.')
        self.assertEqual(self.sword.value, 5)
        self.assertEqual(self.sword.damage, 10)


class DraggerWeaponTests(WeaponTests):
    """ Test Dagger Information And Damage """

    def setUp(self):
        self.dragger = Dragger()

    def test_init(self):
        self.assertEqual(self.dragger.name, 'Rusty Dragger')
        self.assertEqual(self.dragger.description,
                         'A small dagger with some rust. Be better if you could throw the dragger.')
        self.assertEqual(self.dragger.value, 10)
        self.assertEqual(self.dragger.damage, 15)


class AxeWeaponTests(WeaponTests):
    """ Test Axe Information And Damage """

    def setUp(self):
        self.axe = Axe()

    def test_init(self):
        self.assertEqual(self.axe.name, 'Axe of Echo')
        self.assertEqual(self.axe.description,
                         'A weapon abandoned by a famous adventure. Pretty good axe.')
        self.assertEqual(self.axe.value, 15)
        self.assertEqual(self.axe.damage, 25)


class NightSwordWeaponTests(WeaponTests):
    """ Test Axe Information And Damage """

    def setUp(self):
        self.night_sword = NightSword()

    def test_init(self):
        self.assertEqual(self.night_sword.name, "Night's Edge")
        self.assertEqual(self.night_sword.description,
                         'A black sword with a snake style blade that deals deadly damage.')
        self.assertEqual(self.night_sword.value, 25)
        self.assertEqual(self.night_sword.damage, 35)


# python -m unittest tests/test_items.py
# python -m unittest discover
if __name__ == '__main__':
    unittest.main()
