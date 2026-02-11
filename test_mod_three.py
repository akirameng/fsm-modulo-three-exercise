import unittest
from mod_three import mod_three

class TestModThreeFSM(unittest.TestCase):

    def test_given_examples(self):
        self.assertEqual(mod_three("1101"), 1)
        self.assertEqual(mod_three("1110"), 2)
        self.assertEqual(mod_three("1111"), 0)

    def test_walkthrough_examples(self):
        self.assertEqual(mod_three("110"), 0)
        self.assertEqual(mod_three("1010"), 1)

    def test_edge_cases(self):
        self.assertEqual(mod_three(""), 0)
        self.assertEqual(mod_three("000"), 0)
        self.assertEqual(mod_three("0"), 0)
        self.assertEqual(mod_three("1"), 1)
        self.assertEqual(mod_three("11"), 0)

    def test_large_input(self):
        big_binary = "1" * 10000
        self.assertEqual(mod_three(big_binary), 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            mod_three("102")
        with self.assertRaises(ValueError):
            mod_three("abc")

if __name__ == "__main__":
    unittest.main()
