import unittest
import Q3

class TestCase(unittest.TestCase):
    def test_full_name(self):
        self.assertEqual(Q3.full_name("Korey", "Englert"), "Korey Englert");

    def test_full_name2(self):
        self.assertEqual(Q3.full_name(1, 2), 3);

    def test_full_name3(self):
        self.assertEqual(Q3.full_name(1, 2), "1 2");

    def test_full_name4(self):
        self.assertEqual(Q3.full_name("1", "2"), "12");

    def test_full_name5(self):
        self.assertEqual(Q3.full_name("left", "right"), "left right");
