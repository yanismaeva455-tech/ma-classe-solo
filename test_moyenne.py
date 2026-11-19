import unittest

from moyenne import moyenne_ponderee


class TestMoyenne(unittest.TestCase):
    def test_moyenne_simple(self):
        self.assertEqual(moyenne_ponderee([(10, 1), (20, 1)]), 15.0)

    def test_coefficients(self):
        self.assertEqual(moyenne_ponderee([(10, 1), (16, 2)]), 14.0)

    def test_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne_ponderee([])


if __name__ == "__main__":
    unittest.main()
