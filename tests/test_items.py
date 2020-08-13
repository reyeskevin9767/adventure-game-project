import unittest
from game.items import Item, Gold

# * Testing Items
class BaseItemCases:
    class ItemTests(unittest.TestCase):
        def test_str(self):
            self.assertIsNotNone(str(self))


class GoldTests(BaseItemCases.ItemTests):
    def setUp(self):
        self.gold = Gold(3)

    def test_init(self):
        self.assertEqual(self.gold.name, 'Gold')
        self.assertEqual(self.gold.description, "A Round Coin With 3 stamped on the front.")
        self.assertEqual(self.gold.value, 3)


# python -m unittest tests/test_items.py
# python -m unittest discover -v
if __name__ == '__main__':
    unittest.main()
