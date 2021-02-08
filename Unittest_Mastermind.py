import Logik
import unittest


class TestafLogikogdatalag(unittest.TestCase):

    def test1(self):
        xd = Logik.MastermindLogik()
        self.assertEqual(xd.talkonverter(1), "Rød")

    def test2(self):
        xd = Logik.MastermindLogik()
        self.assertEqual(xd.konverter("Rød"), 1)

    def test3(self):
        xd = Logik.MastermindLogik()
        self.assertEqual(xd.check([1, 3, 5, 7], [1, 2, 3, 4]), ['check', 'wrong', 'half', 'wrong'])



if __name__ == "__main__":
    unittest.main()