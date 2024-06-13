import unittest

from similarity_checker import SimilarityChecker


class SimilarityCheckerTestCase(unittest.TestCase):
    def test_check_letters(self):
        checker = SimilarityChecker()
        checker.set_strings("ASD", "DSA")
        score = checker.check_letters()
        self.assertEqual(score, 60.0)

        checker.set_strings("A", "BB")
        score = checker.check_letters()
        self.assertEqual(score, 0.)


if __name__ == "__main__":
    unittest.main()
