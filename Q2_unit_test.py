import unittest
import Q2

class TestCase(unittest.TestCase):
    def test_average(self):
        self.assertAlmostEqual(Q2.average([3,4,5]), 4);

    def test_average2(self):
        self.assertAlmostEqual(Q2.average([3,4,5]), 5);

    def test_average3(self):
        self.assertAlmostEqual(Q2.average([3.2,4.7,5.1,-.1,100]), 22.58);

    def test_average4(self):
        self.assertAlmostEqual(Q2.average([]), 0);

    def test_average5(self):
        self.assertAlmostEqual(Q2.average(["a","b","c"]), "b");
