import unittest
import Q1

class TestCase(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(Q1.cube(3), 27);

    def test_cube2(self):
        self.assertEqual(Q1.cube(3), 28);

    def test_cube3(self):
        self.assertAlmostEqual(Q1.cube(1.5), 3.375);

    def test_cube4(self):
        self.assertAlmostEqual(Q1.cube(-4), -64);

    def test_cube5(self):
        self.assertEqual(Q1.cube("a"), "aaa");
