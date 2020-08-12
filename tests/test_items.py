import unittest
from game.items import Item

# * Testing Items


class BaseItemCases:
    class ItemTests(unittest.TestCase):
        def setUp(self):
            self.money = Item("Coin", 'A Gold Coin', 2)

        def test_init(self):
            self.assertEqual(self.money.name, 'Coin')
            self.assertEqual(self.money.description, 'A Gold Coin')
            self.assertEqual(self.money.value, 2)

        def test_str(self):
            self.assertIsNotNone(str(self.money))


class GoldTests(BaseItemCases.ItemTests):
    def test_init(self):
        self.amount = 2
        self.assertEqual(self.money.value, self.amount)


# python -m unittest tests/test_items.py
# python -m unittest discover -v
if __name__ == '__main__':
    unittest.main()
