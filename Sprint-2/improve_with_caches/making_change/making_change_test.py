import unittest

from making_change import ways_to_make_change

class MakingChangeTest(unittest.TestCase):
    def test_1(self):
        # 1x 1p
        self.assertEqual(ways_to_make_change(1), 1)

    def test_2(self):
        # 1x 2p
        # 2x 1p
        self.assertEqual(ways_to_make_change(2), 2)

    def test_7(self):
        # 1x 5p, 1x 2p
        # 1x 5p, 2x 1p
        # 3x 2p, 1x 1p
        # 2x 2p, 3x 1p
        # 1x 2p, 5x 1p
        # 7x 1p
        self.assertEqual(ways_to_make_change(7), 6)

    def test_17(self):
        self.assertEqual(ways_to_make_change(17), 28)

    def test_100(self):
        self.assertEqual(ways_to_make_change(100), 4562)
    def test_9176(self):
        self.assertEqual(ways_to_make_change(9176), 628431158425225)

if __name__ == "__main__":
    unittest.main()
