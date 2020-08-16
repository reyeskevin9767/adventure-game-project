import unittest
from enemies import Enemy, FellwoodSpectre, StormGhoul, DreadFiend, ScarletHydra

# * Testing Enemy


class BaseEnemyCases:
    class EnemyTests(unittest.TestCase):
        """ Testing Enemy Template """

        def test_is_alive(self):
            self.assertEqual(self.hp, 0)


class FellwoodSpectreTests(BaseEnemyCases.EnemyTests):
    """ Testing Enemy Information """

    def setUp(self):
        self.spectre = FellwoodSpectre()

    def test_init(self):
        self.assertEqual(self.spectre.name, 'Fellwood Spectre')
        self.assertEqual(self.spectre.hp, 10)
        self.assertEqual(self.spectre.damage, 5)

    def test_is_alive(self):
        self.assertNotEqual(self.spectre.hp, 0)


class StormGhoulTests(BaseEnemyCases.EnemyTests):
    """ Testing Enemy Information """

    def setUp(self):
        self.ghoul = StormGhoul()

    def test_init(self):
        self.assertEqual(self.ghoul.name, 'Storm Ghoul')
        self.assertEqual(self.ghoul.hp, 20)
        self.assertEqual(self.ghoul.damage, 10)

    def test_is_alive(self):
        self.assertNotEqual(self.ghoul.hp, 0)


class DreadFiendTests(BaseEnemyCases.EnemyTests):
    """ Testing Enemy Information """

    def setUp(self):
        self.feind = DreadFiend()

    def test_init(self):
        self.assertEqual(self.feind.name, 'Dread Fiend')
        self.assertEqual(self.feind.hp, 40)
        self.assertEqual(self.feind.damage, 20)

    def test_is_alive(self):
        self.assertNotEqual(self.feind.hp, 0)


class ScarletHydraTests(BaseEnemyCases.EnemyTests):
    """ Testing Enemy Information """

    def setUp(self):
        self.hydra = ScarletHydra()

    def test_init(self):
        self.assertEqual(self.hydra.name, 'Scarlet Hydra')
        self.assertEqual(self.hydra.hp, 60)
        self.assertEqual(self.hydra.damage, 30)

    def test_is_alive(self):
        self.assertNotEqual(self.hydra.hp, 0)


if __name__ == '__main__':
    unittest.main()
