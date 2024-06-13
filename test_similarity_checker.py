import unittest

from similarity_checker import SimilarityChecker


class SimilarityCheckerTestCase(unittest.TestCase):

    def setUp(self):
        self.checker = SimilarityChecker()

    def test_check_letters(self):
        self.assert_equal_score("ASD", "DSA", 40.0)
        self.assert_equal_score("A", "BB", 0.0)

    def assert_equal_score(self, lhs: str, rhs: str, expected_score: float):
        self.checker.set_strings(lhs, rhs)
        score = self.checker.check_letters()
        self.assertEqual(score, expected_score)


if __name__ == "__main__":
    unittest.main()
