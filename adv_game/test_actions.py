import unittest
from actions import MoveUp, MoveLeft, MoveDown, MoveRight
# * Testing Enemy


class BaseActionCases:
    class ActionTests(unittest.TestCase):
        """ Testing Action Template """
        pass


class MoveUpTests(BaseActionCases.ActionTests):
    """ Testing Move Up Information """

    def setUp(self):
        self.move_up = MoveUp()

    def test_init(self):
        self.assertEqual(self.move_up.name, 'Move North')
        self.assertEqual(self.move_up.hotkey, 'w')


class MoveRightTests(BaseActionCases.ActionTests):
    """ Testing Move Right Information """

    def setUp(self):
        self.move_right = MoveRight()

    def test_init(self):
        self.assertEqual(self.move_right.name, 'Move East')
        self.assertEqual(self.move_right.hotkey, 'd')


class MoveDownTests(BaseActionCases.ActionTests):
    """ Testing Move Down Information """

    def setUp(self):
        self.move_down = MoveDown()

    def test_init(self):
        self.assertEqual(self.move_down.name, 'Move South')
        self.assertEqual(self.move_down.hotkey, 's')


class MoveRightTests(BaseActionCases.ActionTests):
    """ Testing Move Left Information """

    def setUp(self):
        self.move_left = MoveLeft()

    def test_init(self):
        self.assertEqual(self.move_left.name, 'Move West')
        self.assertEqual(self.move_left.hotkey, 'a')
